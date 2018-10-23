"""
This method retrieves news from the internet and parses them as News classes.
The process for retrieving News uses NewsAPI
"""

import json
from settings import API_KEY, SOURCES_PT, SEARCH
from models import News
from newsapi import NewsApiClient
from datetime import datetime, timedelta

# Defines dates of interest
DATE_NOW = datetime.strftime(datetime.now() - timedelta(0), '%Y-%m-%d')
DATE_BEFORE = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

# Initialize the API client
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