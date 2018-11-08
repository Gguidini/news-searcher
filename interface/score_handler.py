"""
This module calculates News scores and updates each News with its score.
"""
import functools
from .models import News

def synonyms_pointer(parameters):
    """
    Creates a new list of terms of interest given the dictionary of parameters.
    That's necessary because some parameters have synonyms, and they need to be found too.
    Obviously, a synonym's weight is the same of the respective word.

    Arguments>
    > paramenters : dict
        The dictionary with terms of interest, their synonyms, and their weight score.
    """

    pointers = []
    for k, v in parameters.items():
        pointers.append( (k,k)) # a word of interest points to itself
        for synonym in v[0]: # v[0] is the list of synonyms
            pointers.append( (synonym, k))
    return pointers

def synonyms_pointer2(parameters):
    """
    Creates a new list of terms of interest given the dictionary of parameters.
    That's necessary because some parameters have synonyms, and they need to be found too.
    Obviously, a synonym's weight is the same of the respective word.

    Arguments>
    > paramenters : dict
        The dictionary with terms of interest, their synonyms, and their weight score.
    """

    pointers = {}
    for k, v in parameters.items():
        pointers[k] = k # a word of interest points to itself
        for synonym in v[0]: # v[0] is the list of synonyms
            pointers[synonym] = k
    return pointers

def create_counter(parameters):
    return  {key: 0 for key in parameters}

def score_news(article : News, parameters, pointers = None):
    """
    Given a news article, calculates its score and updates it.
    The score is calculated has follows:
    1. Every word of interest has weights assigned to it, considering different categories.
    2. The number of times a word of interest appears in the content or title of an article is computed.
    3. The weighted average is calculated, considering the total points a words can receive:
        (a * (w[1]/5) + ... + a * (w[7]/5))
        a is the number of times word was found / number of words in article,
        w[i] is weight for ith category,
        5 is the maximum weight points for a category,
    4. The resulting score is added to the article's score.

    Arguments:
    > article : News
        The article to be scored
    > parameters : dict
        The dictionary with the terms of interest and their weights in each category.
    """
    # gets all list of words of interest
    if pointers == None:
        pointers = synonyms_pointer(parameters)

    # amount of words in the article, for normalization purposes
    words = len(article.title.split(' ')) + len(article.content.split(' '))

    # score of article
    score = 0

    for (word_of_interest, reference) in pointers:
        p_value = parameters[reference][1:] # weights in categories.
        # When word appears in title is given more value
        apparitions = (article.title.lower().count(word_of_interest) * 3) + article.content.lower().count(word_of_interest)
        # Normalization on word count
        apparitions /= words
        # score
        score_increment = 0
        for v in p_value:
            score_increment += (v/5) * apparitions
        score += (score_increment)
    
    article.score = score

def score_news2(article : News, parameters, pointers = None, apparitions = None):

    if pointers == None:
        pointers = synonyms_pointer2(parameters)

    if apparitions == None:
        apparitions = create_counter(parameters)

    total = article.title.lower().split() + article.content.lower().split()

    for word in total:
        if word in pointers:
            apparitions[pointers[word]] += 1


    # amount of words in the article, for normalization purposes
    words = len(article.title.split(' ')) + len(article.content.split(' '))

    # score of article
    score = 0

    for reference,apparition in apparitions.items():
        p_value = parameters[reference][1:] # weights in categories.
        
        apparitions[reference] /= words
        
        score_increment = 0
        
        for v in p_value:
            score_increment += (v/5) * apparition
        
        score += (score_increment)
    return score
