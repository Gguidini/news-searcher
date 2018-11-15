from django.shortcuts import render
import interface.src.data_output as output
import interface.src.news_handler as news_handler
import interface.src.score_handler as score_handler
from interface.src.config import API_KEY, SOURCES, TERMS
from interface.src.config import updateKey, addSource, addTerm, removeSource, removeTerm


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
            updateKey(request.POST.get("api"))
        # adiciona uma nova source ao arquivo
        elif 'source' in request.POST and request.POST.get("source") not in SOURCES:
            addSource(request.POST.get("source"))
        # remove uma fonte do arquivo
        elif 'delete_source' in request.POST:
            removeSource(request.POST.get("delete_source"))
        # adiciona um novo termo ao arquivo
        elif 'term' in request.POST and request.POST.get("term") not in TERMS:
            term = request.POST.get("term").lower()
            sinonimo = request.POST.get("sinonimo").lower()
            t = request.POST.get("tech")
            p = request.POST.get("politics")
            e = request.POST.get("economics")
            d = request.POST.get("dissemination")
            i = request.POST.get("impact")
            s = request.POST.get("severity")
            c = request.POST.get("current")
            addTerm(term, sinonimo, t, p, e, d, i, s, c)
        # remove um termo do arquivo
        elif 'delete_term' in request.POST:
            removeTerm(request.POST.get("delete_term"))
        
    return render(request, 'settings.html', {'key':API_KEY, 'sources':SOURCES, 'terms':TERMS})

def result(request):
    """
    Displays search results.
    """
    data = {}
    if request.method == 'GET':
        valid_terms = request.GET.getlist("valid_term")
        valid_sources = request.GET.getlist("valid_source")

    # select only the valid terms
    valid_terms = { term: TERMS.get(term) for term in valid_terms }
    
    # get the initialized api client 
    client = news_handler.api_client(API_KEY)
    if client == None:
        return render(request, 'key_error.html', {})
    # store all news to send to data['results']
    results = []
    # quantity of news
    size = 0
    # search for all terms in all sources
    for term in valid_terms:
        s, r = news_handler.get_query_articles(client, term, valid_sources)
        size += s
        results += r

    # insert sorted news
    if size > 0:
        for n in results:
            score_handler.score_news(n, valid_terms)

    results = sorted(results, reverse = True)
    
    # Uncomment to test production of docx file
    # File will be saved in interface/tmp/ with name clipping + today's date
    #output.create_docx(results, 'interface/tmp/')
    
    return render(request, 'results.html', {'size':size, 'results':results})

