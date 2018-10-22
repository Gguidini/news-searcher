"""
This method retrieves news from the internet and parses them as News classes.
The process for retrieving News uses NewsAPI
"""

from settings import API_KEY, SOURCES_PT, DATE_NOW, DATE_BEFORE, SEARCH
from models import News
from newsapi import NewsApiClient
import json

# Init
newsapi = NewsApiClient(api_key=API_KEY)

# get everything
all_articles = newsapi.get_everything(q=SEARCH,
                                      domains=','.join(SOURCES_PT),
                                      from_param=DATE_BEFORE,
                                      to=DATE_NOW,
                                      language='pt',
                                      sort_by='relevancy')

with open("../news/todos_artigos.json", 'w', encoding='utf8') as outfile:
    json.dump(all_articles, outfile, indent=4, sort_keys=True, ensure_ascii=False)