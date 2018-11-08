from interface.news_handler import api_client, get_all_articles
import interface.score_handler
from interface.config import API_KEY, SOURCES, TERMS
from interface.config import updateKey, addSource, addTerm, removeSource, removeTerm
from django.shortcuts import render

data = {}
data['key'] = API_KEY
data['sources'] = SOURCES
data['terms'] = TERMS

def index(request):
    return render(request, 'index.html', data)

def settings(request):
    if request.method == 'POST':
        # faz o update da chave da API
        if 'api' in request.POST:
            data['key'] = updateKey(request.POST.get("api"))
        # valida quais das sources vai ser a utilizada
        elif 'valid_source' in request.POST:
            data['sources'] = request.POST.getlist("valid_source")
        # adiciona uma nova source ao arquivo
        elif 'source' in request.POST and request.POST.get("source") not in data['sources']:
            data['sources'] = addSource(request.POST.get("source"))
        # adiciona um novo termo ao arquivo
        elif 'term' in request.POST and request.POST.get("term") not in data['terms']:
            data['terms'] = addTerm(request.POST.get("term"))
        # remove um termo do arquivo
        elif 'delete_term' in request.POST:
            data['terms'] = removeTerm(request.POST.get("delete_term"))
        # BOTAO RESTAURAR - volta todas as fontes e termos a como esta nos arquivos
        else:
            data['sources'] = SOURCES
            data['terms'] = TERMS
    return render(request, 'settings.html', data)

def result(request):
    if request.method == 'GET':
        # busca pela barra de pesquisa
        if 'term' in request.GET:
            data['terms'] = [request.GET.get("term")]
        # busca os termos checkados
        else:
            data['terms'] = request.GET.getlist("valid_term")
    client = api_client(str(data['key']))
    results = []
    # adiciona todos os termos ao result
    for term in data['terms']:
        results += get_all_articles(client, term, data['sources'])[1]
    data['results'] = results
    return render(request, 'results.html', data)