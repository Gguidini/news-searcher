from django.shortcuts import render
import interface.src.data_output as output
import interface.src.news_handler as news_handler
import interface.src.score_handler as score_handler
from interface.src.config import API_KEY, SOURCES, TERMS
from interface.src.config import updateKey, addSource, addTerm, removeSource, removeTerm


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
        # adiciona uma nova source ao arquivo
        elif 'source' in request.POST and request.POST.get("source") not in data['sources']:
            data['sources'] = addSource(request.POST.get("source"))
        # remove uma fonte do arquivo
        elif 'delete_source' in request.POST:
            data['sources'] = removeSource(request.POST.get("delete_source"))
        # adiciona um novo termo ao arquivo
        elif 'term' in request.POST and request.POST.get("term") not in data['terms']:
            term = request.POST.get("term")
            sinonimo = request.POST.get("sinonimo")
            t = request.POST.get("tech")
            p = request.POST.get("politics")
            e = request.POST.get("economics")
            d = request.POST.get("dissemination")
            i = request.POST.get("impact")
            s = request.POST.get("severity")
            c = request.POST.get("current")
            data['terms'] = addTerm(term, sinonimo, t, p, e, d, i, s, c)
        # remove um termo do arquivo
        elif 'delete_term' in request.POST:
            data['terms'] = removeTerm(request.POST.get("delete_term"))
        
    return render(request, 'settings.html', data)

def result(request):
    if request.method == 'GET':
        data['terms'] = request.GET.getlist("valid_term")
        data['sources'] = request.GET.getlist("valid_source")
    client = news_handler.api_client(str(data['key']))
    if client == None:
        return render(request, 'key_error.html', {})
    results = []
    size = 0

    # busca por todos os termos em todas as fontes
    for term in data['terms']:
        s, r = news_handler.get_all_articles(client, term, data['sources'])
        size += s
        results += r
    
    


    final = []
    for i in range (len(results)):
        nota = score_handler.ssrc_news2(results[i],TERMS,None,None)
        #final.append(score_handler.ssrc_news2(results[i],TERMS,None,None),results[i],size[i])
        print('Nota da noticia %i = ' %i + str(nota))
    #final.sort()

    #for sortedNews in final:
    #    data['results'].append(sortedNews[1])
    #    data['size'].append(sortedNews[2])

    data['results'] = results
    data['size'] = size
    
    # Uncomment to test production of docx file
    # File will be saved in docs/ with name clipping + today's date
    #output.create_docx(results, 'docs/')

    #volta com os termos do arquivo
    data['sources'] = SOURCES
    data['terms'] = TERMS
    
    return render(request, 'results.html', data)