"""
This is the 'main loop' for the news searcher system.
Uses CherryPy running on localserver to create an easy-to-use interface.
"""

import cherrypy
import template_bits
from settings import API_KEY, SOURCES

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        with open('assets/index.html', 'r') as fd:
            template = fd.read()
        return template

    @cherrypy.expose
    def settings(self, **kargs):
        template = template_bits.header()
        template += template_bits.api_key_form(API_KEY)
        template += template_bits.sources_form(SOURCES)
        if kargs == {}:
            return template # mostra a view
        else:
            return str(kargs) # mostra o q veio do request. Somente teste. Futuramente deve processar mudanças e mostrar a view novamente

    @cherrypy.expose
    def search(self):
        return "Search!"


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())