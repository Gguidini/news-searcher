"""
This module controls all views for the system.
Each view has a different function assigned to it.
"""

import os
import pickle
import importlib

from django.shortcuts import render

import interface.src.config as config
import interface.src.data_output as data_output
import interface.src.news_handler as news_handler
import interface.src.score_handler as score_handler

from interface.src.config import SOURCES, TERMS
from news_searcher.settings import MEDIA_ROOT


def API_KEY():
    """
    Load the API KEY from file
    so Django cache doens't pick the wrong one 
    """
    return pickle.load(open(os.path.join("interface", "src", "bins", "api-key.bin"), "rb"))


def index(request):
    """
    Index page.
    Shows SOURCES and TERMS
    so that user may choose what term to search for, and what sourcer to search in.
    """
    return render(request, 'index.html', {'sources':SOURCES, 'terms':TERMS})

def settings(request):
    """
    System settings.
    Allows user to change:
        1. API KEY
        2. List of trustworthy sources
        3. List of terms, their weights and synonyms
    """

    if request.method == 'POST':
        # faz o update da chave da API
        if 'api' in request.POST:
            config.updateKey(request.POST.get("api"))
        # adiciona uma nova source ao arquivo
        elif 'source' in request.POST and request.POST.get("source") not in SOURCES:
            config.addSource(request.POST.get("source"))
        # remove uma fonte do arquivo
        elif 'delete_source' in request.POST:
            config.removeSource(request.POST.get("delete_source"))
        # adiciona um novo termo ao arquivo
        elif 'term' in request.POST and request.POST.get("term") not in TERMS:
            term = request.POST.get("term").lower()
            sinonimos = request.POST.get('sinonimo').lower()
            sinonimos = sinonimos.split("\r\n")
            t = request.POST.get("tech")
            p = request.POST.get("politics")
            e = request.POST.get("economics")
            d = request.POST.get("dissemination")
            i = request.POST.get("impact")
            s = request.POST.get("severity")
            c = request.POST.get("current")
            config.addTerm(term, sinonimos, t, p, e, d, i, s, c)
        # remove um termo do arquivo
        elif 'delete_term' in request.POST:
            config.removeTerm(request.POST.get("delete_term")) 
        # atualiza informações do banco de dados
        elif 'bd_url' in request.POST:
            config.updateBD(request.POST.get('bd_url'), request.POST.get('bd_passwd'))
            importlib.reload(config) # Reload information updated
    (BD_URL, BD_PASSWD) = config.BD_INFO()
    return render(request, 'settings.html', {'key': API_KEY(), 'sources':SOURCES, 'terms':TERMS,                                      'bd_url':BD_URL, 'bd_passwd':BD_PASSWD})

def result(request):
    """
    Displays search results.
    """
    valid_terms = request.GET.getlist("valid_term")
    valid_sources = request.GET.getlist("valid_source")
    # Get all info on terms of interest
    valid_terms = { term: TERMS.get(term) for term in valid_terms }
    # Initialize API Client, of redirect to error page 
    client = news_handler.api_client(API_KEY())
    if client is None:
        return render(request, 'key_error.html', {})
    # List of News and size of response
    results = {}
    size = 0
    # search for all valid terms in all valid sources
    for term in valid_terms:
        s, r = news_handler.get_query_articles(client, term, valid_sources)
        size += s
        results[term] = r

    # Sort News
    for key, item in results.items(): # dictionary of news per term
        for n in item: # list of news
            n.disease = key # add term to News
            score_handler.score_news(n, valid_terms) # score news
        results[key] = sorted(item, reverse=True) # sort News
    # Save News temporarily to await selection
    pickle.dump(results, open(os.path.join('interface', 'src', 'bins', 'latest_news.bin'), 'wb'))
    
    return render(request, 'results.html', {'size':size, 'results':results})

def clear_tmp_folder():
    """
    Delete all .docx files in the media directory.
    """
    tmp = MEDIA_ROOT
    for f in os.listdir(tmp):
        if f.endswith('.docx'):
            os.remove(os.path.join(tmp, f))

def output(request):
    """
    Creates the docx document and pushes selected News to database.
    """
    dict_of_news = pickle.load(open(os.path.join('interface', 'src', 'bins', 'latest_news.bin'), 'rb'))
    valid_results = request.POST.getlist('valid_result')
    all_news = []
    valid_news = []
    for key, item in dict_of_news.items():
        all_news += item # throw all news in a single list
    # Separate only valid news
    for n in all_news:
        if n.url in valid_results:
            n.region = request.POST.get('region_{}'.format(n.url))
            valid_news.append(n)

    # Connection with database
    errors = [] # records if news can't go to DB.
    for n in valid_news:
        err = data_output.push_to_DB(n)
        print(err.text)
        if err.text.startswith('Fail'):
            errors.append('ERRO adicionando notícia: {}'.format(n.title))

    if errors == []:
        errors = ['Todas as notícias foram adicionadas ao Banco de Dados!']
    # Remove any previous clipping to avoid cluttering
    clear_tmp_folder()
    # New clipping will be saved in interface/tmp/ with name clipping + today's date
    out = data_output.create_docx(valid_news, MEDIA_ROOT)

    return render(request, 'output.html', {'news':valid_news, 'size':len(valid_news), 'file':out, 'error':errors})
