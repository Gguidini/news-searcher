"""
Tests for score_handler module
"""
import unittest
import json
from context import SCORER, MODELS

class TestScoreHandler(unittest.TestCase):
    """
    Unit tests for score handler module.
    """

    def test_synonims(self):
        """
        Tests that, given a data dictionary, the function correctly returns all words of interest.
        Return is (word_of_interest, reference_in_dict).
        Some words may have synonyms.
        """

        reference = {
            'aids' : [['hiv'], 0, 0, 0, 1, 1, 5, 3],
            'botulismo' : [[], 0, 0, 0, 1, 1, 4, 1],
            'dengue' : [[], 0, 0, 0, 1, 1, 3, 3],
            'dst' : [['std'], 0, 0, 0, 1, 1, 1, 2]
        }
        word_list = SCORER.synonyms_pointer(reference)
        self.assertTrue(isinstance(word_list[0], tuple))
        self.assertEqual(6, len(word_list))
        self.assertEqual(('aids', 'aids'), word_list[0])
        self.assertEqual(('hiv', 'aids'), word_list[1])

    def test_scoring(self):
        """
        Test for score_news method. Given a list of parameters,
        and a News article, calculates its score.
        """
        reference = {
            'aids' : [['hiv'], 0, 0, 0, 1, 1, 5, 3],
            'dengue' : [[], 0, 0, 0, 1, 1, 3, 3],
            'saúde' : [['health'], 0, 0, 1, 2, 3, 3],
            'crise' : [[], 1, 1, 1, 1, 0, 0, 0],
            'câncer' : [[], 2, 1, 1, 3, 1, 5, 5],
        }
        pointers = SCORER.synonyms_pointer(reference)
        # Create some News
        with open('articles_example.json', 'r') as fd:
            raw_news = fd.read()
        json_news = json.loads(raw_news)
        results = json_news['totalResults']
        news = []
        for article in json_news['articles']:
            news.append(MODELS.News.from_json(article))
        # Verify that score starts at 0
        for n in news:
            self.assertEqual(0, n.score)
        
        # Calculates new scores from reference
        for n in news:
            SCORER.score_news(n, reference, pointers)
            self.assertTrue(n.score > 0)    # verify that scores changed
        
        


# Runs tests when executing file
if __name__ == '__main__':
    unittest.main()