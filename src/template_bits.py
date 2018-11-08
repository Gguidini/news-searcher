"""
Defines a few functions to make it easier to generate parts of the HTMLS served.
"""

def header(title='Title', links=[], script="", style=""):
    """
    An HTML header has a title tag, and may contain several links to the page.
    This function returns the html code for a <head> tag, with title.
    links should be linking the page to static files, e.g. scripts, css.
    """
    HEAD = """<!DOCTYPE html>
        <!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
        <!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
        <!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
        <!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
            <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="description" content="">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        """
    SCRIPT = '<script>' + script + '</script>'
    STYLE = '<style>' + style + '</style>'
    TAIL = '</head>'
    return HEAD + "\n".join(links) + SCRIPT + STYLE  + TAIL

def body(inner_html, script):
    """
    Returns a body with given html and the script.
    """
    return '<body id="body">' + inner_html + '<script>' + script + '</script></body>'

def create_link(file_name, type):
    """
    Created the html for a link given a src name.
    """
    if type == 'script':
        return '<script src="' + file_name +'"></script>'
    else:
        return '<link rel="stylesheet" href="'+ file_name +'">'
