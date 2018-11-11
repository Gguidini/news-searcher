"""
This module defines a few essential constants for the system.
To use the constants in different modules import the constant you want.

> Exemple
from settings import API_KEY

DON'T CHANGE THE VALUES IN THIS MODULE UNLESS YOU KNOW WHAT YOU'RE DOING.
"""
import pickle

API_KEY = pickle.load(open("interface/src/bins/api-key.bin", "rb"))

SOURCES = pickle.load(open("interface/src/bins/sources.bin", "rb"))

TERMS =  pickle.load(open("interface/src/bins/terms.bin", "rb"))

# Words of interest and their respective weight value.
# Weights are ranged from 0 to 5.
# There are 7 diffent 'interest categories', so formatting is like follows:
# word : [ [synonyms], sci/tech, politics, economics, dissemination, impact, severity, current interest]
# every key is a word of interest in an article.
SCORE_VALUES = {
    'aids' : [['hiv'], 0, 0, 0, 1, 1, 5, 3],
    'botulismo' : [[], 0, 0, 0, 1, 1, 4, 1],
    'dengue' : [[], 0, 0, 0, 1, 1, 3, 3],
    'dst' : [['std'], 0, 0, 0, 1, 1, 1, 2]
}


def updateKey(new_key):
    API_KEY = new_key
    pickle.dump(API_KEY, open("interface/bins/api-key.bin", "wb"))
    return API_KEY

def addSource(source):
    SOURCES.append(str(source))
    pickle.dump(SOURCES, open("interface/bins/sources.bin", "wb"))
    return SOURCES

def removeSource(source):
    SOURCES.remove(str(source))
    pickle.dump(SOURCES, open("interface/bins/sources.bin", "wb"))
    return SOURCES

def addTerm(term):
    TERMS.append(str(term))
    pickle.dump(TERMS, open("interface/bins/terms.bin", "wb"))
    return TERMS

def removeTerm(term):
    TERMS.remove(str(term))
    pickle.dump(TERMS, open("interface/bins/terms.bin", "wb"))
    return TERMS
