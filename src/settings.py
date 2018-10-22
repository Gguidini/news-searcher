"""
This module defines a few essential constants for the system.
To use the constants in different modules import the constant you want.

> Exemple
from settings import API_KEY

DON'T CHANGE THE VALUES IN THIS MODULE UNLESS YOU KNOW WHAT YOU'RE DOING.
"""

import os
from datetime import datetime, timedelta

# To specify new paths in the project use os.path.join( BASE_DIR, 'new_path')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_KEY = ''

SOURCES_PT = ['globo.com','gazetaweb.globo.com','uol.com.br','terra.com.br','tribunadonorte.com.br','r7.com','ebc.com.br','abril.com.br','estadao.com.br','correiobraziliense.com.br']

TERMS = []

DATE_NOW = datetime.strftime(datetime.now() - timedelta(0), '%Y-%m-%d')

DATE_BEFORE = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

SEARCH = input("Qual o principal termo da noticia buscada: ")