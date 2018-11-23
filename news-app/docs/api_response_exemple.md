# The NewsAPI

News API is a simple and easy-to-use API that returns JSON metadata for headlines and articles live all over the web right now.

We will be using the News API in this project to search for the News we need.
For more information visit the [News API](https://newsapi.org/) website.

# The newsapi-python

NewsAPI has a simple python library to make it easier to use. We are using such library in our project. 
For more information visit the [newsapi-python](https://newsapi.org/docs/client-libraries/python) webpage.

# Result Example

The result of a query is a json object. An example of such object is:
```json
{
    "articles": [
        {
            "author": "Guilherme Dearo",
            "content": "São Paulo – Segundo uma pesquisa recente do Datafolha, saúde é a maior preocupação dos brasileiros, com 23% da população (quase um entre quatro) citando a questão como a mais importante da atualidade. Saúde superou segurança, que dominava a lista das maiores … [+13778 chars]",
            "description": "EXAME entrevistou especialistas na área de saúde para analisar a qualidade e viabilidade das propostas de Bolsonaro e Haddad",
            "publishedAt": "2018-10-21T09:00:05Z",
            "source": {
                "id": null,
                "name": "Abril.com.br"
            },
            "title": "O que propõem Haddad e Bolsonaro para a Saúde, maior preocupação nacional",
            "url": "https://exame.abril.com.br/brasil/o-que-propoem-haddad-e-bolsonaro-para-a-saude-maior-preocupacao-nacional/",
            "urlToImage": "https://abrilexame.files.wordpress.com/2016/09/size_960_16_9_protestos18.jpg?quality=70&strip=info&w=680&h=453&crop=1"
        }
    ],
    "status": "ok",
    "totalResults": 1
```
