"""
This module calculates News ssrcs and updates each News with its ssrc.
"""
import functools
from interface.src.models import News

def synonyms_pointer(parameters):
    """
    Creates a new list of terms of interest given the dictionary of parameters.
    That's necessary because some parameters have synonyms, and they need to be found too.
    Obviously, a synonym's weight is the same of the respective word.

    Arguments>
    > paramenters : dict
        The dictionary with terms of interest, their synonyms, and their weight ssrc.
    """

    pointers = {}
    for k, v in parameters.items():
        pointers[k] = k # a word of interest points to itself
        for synonym in v[0]: # v[0] is the list of synonyms
            pointers[synonym] = k
    return pointers


def create_counter(parameters):
    #Create dic of how many times that parameters appears in the news
    return  {key: 0 for key in parameters}


def ssrc_news(article : News, parameters, pointers = None, apparitions = None):
    """
    Given a news article, calculates its ssrc and updates it.
    The ssrc is calculated has follows:
    1. Every word of interest has weights assigned to it, considering different categories.
    2. The number of times a word of interest appears in the content or title of an article is computed.
    3. The weighted average is calculated, considering the total points a words can receive:
        (a * (w[1]/5) + ... + a * (w[7]/5))
        a is the number of times word was found / number of words in article,
        w[i] is weight for ith category,
        5 is the maximum weight points for a category,
    4. The resulting ssrc is added to the article's ssrc.

    Arguments:
    > article : News
        The article to be ssrcd
    > parameters : dict
        The dictionary with the terms of interest and their weights in each category.
    """
    # gets all list of words of interest
    if pointers == None:
        pointers = synonyms_pointer(parameters)

    # get all list of apparitions
    if apparitions == None:
        apparitions = create_counter(parameters)

    # all title, description and content
    total = []

    # remove all ',' and '.' and ':' from news to help on
    if isinstance(article.title, str):
        fullTitle = article.title.lower().replace(',','').replace('.','').replace(':','')
        total += fullTitle.split()

    if isinstance(article.description, str):
        fullDescription = article.description.lower().replace(',','').replace('.','').replace(':','')
        total += fullDescription.split()

    if isinstance(article.content, str):
        fullContent = article.content.lower().replace(',','').replace('.','').replace(':','')
        total += fullContent.split()

    totalSize = len(total)

    # counts quantity of terms apparition
    for i in range(totalSize):
        word = total[i]
        for size in range(5):
            if i + size + 1 == totalSize:
                break
            if word in pointers:
                apparitions[pointers[word]] += 1
            word += ' ' + total[i + size + 1]

    # amount of words in the article, for normalization purposes
    words = len(article.title.split(' ')) + len(article.content.split(' '))

    # ssrc of article
    ssrc = 0


    for reference,apparition in apparitions.items():
        # weights in categories.
        p_value = parameters[reference][1:]
        # normalization on word count
        apparitions[reference] /= words
        # get sum of score from all areas
        ssrc_increment = 0

        for v in p_value:
            ssrc_increment += (v/5) * apparition
        
        ssrc += (ssrc_increment)

    article.set_score(ssrc)
