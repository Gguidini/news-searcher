import interface.src.news_handler as news_handler
import interface.src.score_handler as score_handler
import interface.src.data_output as output
from interface.src.config import API_KEY, SOURCES, TERMS
from interface.src.config import updateKey, addSource, addTerm, removeSource, removeTerm
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
    client = news_handler.api_client(str(data['key']))
    results = []
    # adiciona todos os termos ao result
    size = 0
    results = []
    for term in data['terms']:
        s, r = news_handler.get_all_articles(client, term, data['sources'])
        size += s
        results += r
    data['results'] = results
    data['size'] = size
    # Uncomment to test production of docx file
    # File will be saved in docs/ with name clipping + today's date
    #output.create_docx(results, 'docs/')
    return render(request, 'results.html', data)