"""
This file allows other test files in this directory to access
the code in 'src' folder.

Something not very nice happens that it doesn't show the src submodules.
So the solution is to use the constants that are parts of the src modules.

Example:
> from context import MODELS
"""
import os
import sys

# Expands import paths for the tests folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# imports the src folder
import src.models

MODELS = src.models
