"""
This method retrieves news from the internet and parses them as News classes.
The process for retrieving News uses NewsAPI
"""

from settings import API_KEY
from models import News
from newsapi import NewsApiClient
import json

# Init
newsapi = NewsApiClient(api_key=API_KEY)

# get everything
all_articles = newsapi.get_everything(q='dengue',
                                      domains='globo.com,gazetaweb.globo.com,uol.com.br,terra.com.br,tribunadonorte.com.br,r7.com,ebc.com.br,abril.com.br,estadao.com.br,correiobraziliense.com.br',
                                      from_param='2018-10-20',
                                      to='2018-10-21',
                                      language='pt',
                                      sort_by='relevancy')

with open("../news/todos_artigos.json", 'w', encoding='utf8') as outfile:
    json.dump(all_articles, outfile, indent=4, sort_keys=True, ensure_ascii=False)