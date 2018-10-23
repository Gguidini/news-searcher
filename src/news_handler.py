"""
This method retrieves news from the internet and parses them as News classes.
The process for retrieving News uses NewsAPI
"""

import json
from settings import API_KEY, SOURCES, SEARCH # Esses imports aqui va=ão pro main.py no futuro
from models import News
from newsapi import NewsApiClient
from datetime import datetime, timedelta

# Defines dates of interest
DATE_NOW = datetime.strftime(datetime.now() - timedelta(0), '%Y-%m-%d')
DATE_BEFORE = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

# Initialize the API client
newsapi = NewsApiClient(api_key=API_KEY)

# get everything
def get_every_article():
    """
    Returns a list of News from results, and the number of results expected.
    """
    articles = newsapi.get_everything(q=SEARCH,
                     domains=','.join(SOURCES),
                        from_param=DATE_BEFORE,
                                   to=DATE_NOW,
                           sort_by='relevancy')
    results = articles['totalResults']
    news = []
    for article in articles['articles']:
        news.append(News.from_json(article))
    return (results, news)



def get_top_article():
    """
    Returns a list of the top headline News
    """
    articles = newsapi.get_top_headlines(q=SEARCH,
                                          country='br',
                                          category='health')