"""
This method retrieves news from the internet and parses them as News classes.
The process for retrieving News uses NewsAPI
"""

import json
from interface.models import News
from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException
from datetime import datetime, timedelta
from typing import List # used for type hinting

# Defines dates of interest
DATE_NOW = datetime.strftime(datetime.now() - timedelta(0), '%Y-%m-%d')
DATE_BEFORE = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

# Initialize the API client
def api_client(api_key : str):
    """
    Initializes a new api client and returns it, or an error.
    To detect the error, it performs a test query. If query is successful, returns client,
    if query fails, returns Error.
    """

    newsapi = NewsApiClient(api_key=api_key)
    # test query
    try:
        newsapi.get_sources()
        return newsapi
    except NewsAPIException:
        return None

# get everything
def get_query_articles(newsapi, search : str, sources : List[str]):
    """
    Returns a list of News from results, and the number of results expected.

    Arguments:
    > newsapi : NewsApiClient
        The NewsApi Client, necessary to contact the api and run the queries.
    > search : string
        The search string to look for. Terms of interest.
    > sources : list
        The sources in which to look for search.
    """
    
    articles = newsapi.get_everything(q=search,
                     domains=','.join(sources),
                        from_param=DATE_BEFORE,
                                   to=DATE_NOW,
                           sort_by='relevancy')
    results = articles['totalResults']
    news = []
    for article in articles['articles']:
        news.append(News.from_json(article))
    return (results, news)

def get_top_articles(newsapi, search : str):
    """
    Returns a list of the top headline News, and the number of results.

    Arguments:
    > newsapi : NewsApiClient
        The NewsApi Client, necessary to contact the api and run the queries.
    > search : string
        The search term to look for.
    """

    articles = newsapi.get_top_headlines(q=search,
                                          country='br',
                                          category='health')
    results = articles['totalResults']
    news = []
    for article in articles['articles']:
        news.append(News.from_json(article))
    return (results, news)

def get_all_articles(newsapi, search : str, sources : List[str]):
    """
    Returns both the top headlines and query articles.
    Makes use of functions get_query_articles and get_top_articles.

    Arguments:
    > newsapi : NewsApiClient
        The NewsApi Client, necessary to contact the api and run the queries.
    > search : string
        The search string to look for. Terms of interest.
    > sources : list
        The sources in which to look for search
    """

    (r, n) = get_query_articles(newsapi, search, sources)
    (rt, nt) = get_top_articles(newsapi, search)
    return (r + rt, n + nt)