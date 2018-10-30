"""
Tests for news_handler module.
"""

import unittest
from context import HANDLER # HANDLER is the news_handler module
from context import MODELS # To verify that the articles are News instances.

class TestNewsHandler(unittest.TestCase):
    """
    UNIT TESTS for news_handler module
    """

    API_KEY = 'aa40d5c0ed5b4673a9798bf080ccbc34' # the self.API_KEY. It can become invalid over time!

    def test_client(self):
        """
        Tests the correct use of the NewsApiClient.
        ATTENTION - SUBJECT TO THE VALIDITY OF self.API_KEY !!!
        """

        # failure situation
        self.assertEqual(None, HANDLER.api_client('invalid key'))
        # working situation
        self.assertNotEqual(None, HANDLER.api_client(api_key=self.API_KEY), "Error creating the API Client. Verify that the api_key is valid.")

    def test_query_news(self):
        """
        Tests that news can be retrieved from the API.
        """
        client = HANDLER.api_client(api_key=self.API_KEY)
        (response_size, article_list) = HANDLER.get_query_articles(client, 'saúde', ['globo', 'google-news-br', 'Bahianoticias.com.br', 'Diariodoscampos.com.br', 'R7.com', 'Atribuna.com.br', 'Metrojornal.com.br', 'Estadao.com.br'])
        self.assertEqual(response_size, len(article_list))
        self.assertEqual( list, type(article_list))
        if response_size > 0:
            self.assertEqual( MODELS.News, type(article_list[0]))

    def test_top_news(self):
        """
        Tests the get top headlines function.
        """

        client = HANDLER.api_client(api_key=self.API_KEY)
        (response_size, article_list) = HANDLER.get_top_articles(client, 'vacina')
        self.assertEqual(response_size, len(article_list))
        self.assertEqual( list, type(article_list))
        self.assertEqual( MODELS.News, type(article_list[0]))

# Runs tests when executing file
if __name__ == '__main__':
    unittest.main()