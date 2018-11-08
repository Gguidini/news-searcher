"""
Defines a few functions to make it easier to generate parts of the HTMLS served.
"""

def header(title='Title', *links, script="", style=""):
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
    return HEAD + "\n".join(links) + TAIL + SCRIPT + STYLE  

def api_key_form(api_key):
    """
    Parser for the api_key form to html.
    """
    HEAD = """<form action="settings" method="post">
            <input type="hidden" name="form-header" value="apikey">
            API KEY: <input type="text" name="apikey" value="
           """
    TAIL = """
            ">
            <input type="submit" value="Submit">
            </form>
           """
    return HEAD + api_key + TAIL

def  sources_form(sources):
    """
    Parser for the sources form to html.
    """
    HEAD = """<form action="settings" method="post">
            <input type="hidden" name="form-header" value="sources">
           """
    DEL_BOX = '<input type="checkbox" name="source_to_del" value="{value}">'
    TAIL = """ 
            <input type="submit" value="Submit">
            </form>
           """
    body = [s + DEL_BOX.format(value=s) for s in sources]
    return HEAD + "\n".join(body) + TAIL

