"""
This module defines a few essential constants for the system.
To use the constants in different modules import the constant you want.

> Exemple
from config import API_KEY

DON'T CHANGE THE VALUES IN THIS MODULE UNLESS YOU KNOW WHAT YOU'RE DOING.
"""
import os
import pickle # uses pickle to save values
from news_searcher.settings import BASE_DIR

SOURCES = pickle.load(open(os.path.join(BASE_DIR,"interface", "src", "bins", "sources.bin"), "rb"))

TERMS =  pickle.load(open(os.path.join(BASE_DIR,"interface", "src", "bins", "terms.bin"), "rb"))

# Words of interest and their respective weight value.
# Weights are ranged from 0 to 5.
# There are 7 diffent 'interest categories', so formatting is like follows:
# word : [ [synonyms], sci/tech, politics, economics, dissemination, impact, severity, current interest]
# every key is a word of interest in an article.
#TERMS = {
#    'aids' : [['hiv'], 0, 0, 0, 1, 1, 5, 3],
#    'botulismo' : [[], 0, 0, 0, 1, 1, 4, 1],
#    'dengue' : [[], 0, 0, 0, 1, 1, 3, 3],
#    'dst' : [['std'], 0, 0, 0, 1, 1, 1, 2]
#}


def updateKey(new_key):
    """
    Updates API KEY to new_key.
    Saves changes in pickle file.
    """
    pickle.dump(new_key, open(os.path.join(BASE_DIR,"interface", "src", "bins", "api-key.bin"), "wb"))

# adicionar uma fonte
def addSource(source):
    """
    Appends new source to SOURCES.
    Saves changes in pickle file.
    """
    SOURCES.append(str(source))
    pickle.dump(SOURCES, open(os.path.join(BASE_DIR,"interface", "src", "bins", "sources.bin"), "wb"))
    return SOURCES

# remover uma fonte
def removeSource(source):
    """
    Remove source fom SOURCES.
    Saves changes in pickle file.
    """
    SOURCES.remove(str(source))
    pickle.dump(SOURCES, open(os.path.join(BASE_DIR,"interface", "src", "bins", "sources.bin"), "wb"))
    return SOURCES

# adicionar um novo termo
def addTerm(term, sinonimos, t, p, e, d, i, s, c):
    """
    Adds new term to TERMS.
    Saves changes in pickle file.
    """
    TERMS[str(term)] = [sinonimos, int(t), int(p), int(e), int(d), int(i), int(s), int(c)]
    pickle.dump(TERMS, open(os.path.join(BASE_DIR,"interface", "src", "bins", "terms.bin"), "wb"))
    return TERMS

# remover um termo
def removeTerm(term):
    """
    Removes term from TERMS.
    Saves changes in pickle file.
    """
    TERMS.pop(str(term))
    pickle.dump(TERMS, open(os.path.join(BASE_DIR,"interface", "src", "bins", "terms.bin"), "wb"))
    return TERMS
