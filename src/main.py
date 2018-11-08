"""
This is the 'main loop' for the news searcher system.
Uses CherryPy running on localserver to create an easy-to-use interface.
"""

import cherrypy
import os
import template_bits
from settings import API_KEY, SOURCES

class NewsSearcherInterface(object):
    @cherrypy.expose
    def index(self):
        with open('assets/index.html', 'r') as fd:
            template = fd.read()
        return template

    @cherrypy.expose
    def settings(self, **kargs):
        links = [template_bits.create_link(l, 'script') for l in ['static/js/apikey_form.js', 'static/js/sources_form.js']]
        template = template_bits.header('Test JS', links)
        form_key = 'api_key_form("' + API_KEY + '");'
        form_sources = 'sources_form([' + ','.join(SOURCES) + ']);'
        template += template_bits.body("", form_key + form_sources)
        template += '</html>'
        if kargs == {}:
            return template # mostra a view
        else:
            return str(kargs) # mostra o q veio do request. Somente teste. Futuramente deve processar mudanças e mostrar a view novamente

    @cherrypy.expose
    def search(self):
        return "Search!"


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './assets'
        }
    }
    cherrypy.quickstart(NewsSearcherInterface(), '/', conf)