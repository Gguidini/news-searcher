"""
This module defines a few essential constants for the system.
To use the constants in different modules import the constant you want.

> Exemple
from settings import API_KEY

DON'T CHANGE THE VALUES IN THIS MODULE UNLESS YOU KNOW WHAT YOU'RE DOING.
"""


API_KEY = 'the all important API KEY'

SOURCES = [
    'globo.com',
    'gazetaweb.globo.com',
    'uol.com.br',
    'terra.com.br',
    'tribunadonorte.com.br',
    'r7.com',
    'ebc.com.br',
    'abril.com.br',
    'estadao.com.br',
    'correiobraziliense.com.br'
]

TERMS = []

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