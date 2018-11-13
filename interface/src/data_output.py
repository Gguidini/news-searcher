"""
This module integrates the system with other systems and 
parses data to the correct output format.
"""
# No integration with News BD yet

import io # image from url
import copy # Table extraction
import requests # Picture recover from url
import datetime

from pathlib import Path # multiplatform integration
from docx import Document   # Accessing and creating documents
from docx.shared import Pt, Cm, RGBColor  # Image and font sizes
from docx.enum.text import WD_ALIGN_PARAGRAPH # paragraph alignment
from docx.enum.style import WD_STYLE_TYPE # style types

# Docx Output

# template document name
ORIGIN = Path('interface/src/assets/template.docx')

# colors RGB values
DARK_GRAY = [0x68, 0x68, 0x68]
BLACK = [0, 0, 0]

def img_from_url(url):
    """
    Returns a binary image from a url
    """
    response = requests.get(url)  
    # Create the picture
    binary_img = io.BytesIO(response.content)  
    return binary_img

def get_template_table(origin):
    """
    Gives a copy of the template table in origin file
    """
    template = Document(origin)
    # Extract template table
    table_skeleton = template.tables[0]
    return copy.deepcopy(table_skeleton)

def add_table(output, table):
    """
    Adds a table to output file.
    """
    table = table._tbl # No idea. Just works
    paragraph = output.add_paragraph() # Create a new paragraph to hold the table
    paragraph._p.addnext(table) # After that, we add the previously copied table

def add_style(doc, style_name, font_family, font_size, rgb, style_type=WD_STYLE_TYPE.CHARACTER, bold=False):
    """
    Creates a new style to be applyed to objects.
    Returns style name.
    """
    obj_styles = doc.styles
    obj_charstyle = obj_styles.add_style(style_name, style_type)
    obj_font = obj_charstyle.font
    obj_font.size = Pt(font_size)
    obj_font.name = font_family
    obj_font.bold = bold
    obj_font.color.rgb = RGBColor(rgb[0], rgb[1], rgb[2])
    return style_name

def change_margins(doc, margin):
    """
    Changes margins of a document to specific size.
    """
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(margin)
        section.bottom_margin = Cm(margin)
        section.left_margin = Cm(margin)
        section.right_margin = Cm(margin)

def format_table(table, article):
    """
    Populates the table correctly from article.
    """
    region = table.cell(0, 2).paragraphs[0]
    title = table.cell(1, 1).paragraphs[0]
    img = table.cell(1, 3).paragraphs[0]
    description = table.cell(2, 1).paragraphs[0]
    thumbnail = table.cell(2, 3).paragraphs[0]
    url = table.cell(3, 0).paragraphs[0]

    region.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    region.add_run('Região Desconhecida', style='regionStyle').bold = True 
    title.add_run(article.title, style='titleStyle').bold = True 
    description.add_run(article.description, style='textStyle')
    url.add_run(article.url, style='urlStyle')

    pic = img_from_url(article.url_to_image)
    img.add_run().add_picture(pic, width=Cm(6), height=Cm(5))

    # thumbnail not working yet
    thumbnail.add_run('tiny img')

def add_centered_img(doc, path, width):
    """
    Adds a new picture to doc, centered.
    """
    doc.add_picture(path, width=width)
    footer_img = doc.paragraphs[-1] # last paragraph, aka the picture
    footer_img.alignment = WD_ALIGN_PARAGRAPH.CENTER

def add_footer(doc):
    """
    Adds the clipping's footer.
    """
    doc.add_picture('interface/src/assets/sala_logo.png', width=Cm(2))
    footer_img = doc.paragraphs[-1] # last paragraph, aka the picture
    footer_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    people_involved = ['Elaboração', 'Tradução', 'Equipe Editorial', 'Revisão']
    for person in people_involved:
        par = doc.add_paragraph(person, style='footerStyle')
        par.bold = True
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER

def create_docx(articles, path_to_output):
    """
    Creates a docx file with tables for each of the article in articles.
    """
    output_name = 'Clipping_' + datetime.date.today().strftime('%a_%d%b%Y')
    output = Document()

    # Adds region bars centered
    add_centered_img(output, 'interface/src/assets/brasil_bar.png', output.sections[0].page_width)
    add_centered_img(output, 'interface/src/assets/mundo_bar.png', output.sections[0].page_width)

    # Create character styles
    add_style(output, 'regionStyle', 'PT Sans', 14, DARK_GRAY)
    add_style(output, 'titleStyle', 'PT Sans', 14, BLACK)
    add_style(output, 'textStyle', 'PT Sans', 12, BLACK)
    add_style(output, 'urlStyle', 'PT Sans', 8, DARK_GRAY)
    # Paragraph style
    add_style(output, 'footerStyle', 'PT Sans', 10, BLACK, WD_STYLE_TYPE.PARAGRAPH, True)

    # Expand margins
    change_margins(output, 1)

    # Copy tables template to output file
    for _ in range(len(articles)):
        add_table(output, get_template_table(ORIGIN))
    # Populate tables
    for idx, article in enumerate(articles):
        print(idx)
        table = output.tables[idx]
        format_table(table, article)

    # Footer
    add_footer(output)

    # Save doc
    path = Path(path_to_output) / (output_name + '.docx')
    output.save(path)
    return path
