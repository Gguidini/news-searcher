"""
This module defines a few essential constants for the system.
To use the constants in different modules import the constant you want.

> Exemple
from settings import API_KEY

DON'T CHANGE THE VALUES IN THIS MODULE UNLESS YOU KNOW WHAT YOU'RE DOING.
"""

import os

# To specify new paths in the project use os.path.join( BASE_DIR, 'new_path')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_KEY = 'API_KEY'
