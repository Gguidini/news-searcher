"""
Test cases for the News class.
"""
import unittest
import json
from context import MODELS

class TestNews(unittest.TestCase):
    """
    Tests the implementation of News class for UNIT TESTS
    """
    def  setUp(self):
        self.news = MODELS.News(source='www.example.com', author='TestCase', title='An article', description='Blah blah blah', url='www.example.com/something', url_to_image='www.example.com/image', published_at='NOW', content='More blah blah blah')
        self.news1 = MODELS.News(source='www.example.com', author='TestCase', title='An article', description='Blah blah blah', url='www.example.com/something', url_to_image='www.example.com/image', published_at='NOW', content='More blah blah blah')
        self.news2 = MODELS.News(source='www.example.com', author='TestCase', title='An article', description='Blah blah blah', url='www.example.com/something', url_to_image='www.example.com/image', published_at='NOW', content='More blah blah blah')
        self.news.set_score(10)
        self.news1.set_score(20)
        self.news2.set_score(20)

    def test_initialization(self):
        """
        Tests if all attributes can be accessed and are correctly tied to their names.
        """
        self.assertEqual('www.example.com', self.news.source)
        self.assertEqual('TestCase', self.news.author)
        self.assertEqual('An article', self.news.title)
        self.assertEqual('Blah blah blah', self.news.description)
        self.assertEqual('www.example.com/something', self.news.url)
        self.assertEqual('www.example.com/image', self.news.url_to_image)
        self.assertEqual('NOW', self.news.published_at)
        self.assertEqual('More blah blah blah', self.news.content)
        self.assertEqual(10, self.news.score)

    def test_comparisons(self):
        """
        Tests implementations of comparison functions with News.
        """
        # equal
        self.assertTrue(self.news1 == self.news2)
        self.assertFalse(self.news == self.news1)
        # less than
        self.assertTrue(self.news < self.news1)
        self.assertFalse(self.news1 < self.news2)
        # less or equal
        self.assertTrue(self.news1 <= self.news2)
        # greater or equal
        self.assertFalse(self.news >= self.news1)
        self.assertTrue(self.news1 >= self.news)
        self.assertTrue(self.news1 >= self.news2)

    def test_news_sort(self):
        """
        Tests sorting News.
        """
        self.news2.set_score(50)
        news_list = [self.news2, self.news1, self.news]
        self.assertEqual([self.news, self.news1, self.news2], sorted(news_list))

    def test_news_from_json(self):
        """
        Tests the creation of a news instance from a json object.
        """
        raw_news = """  {
                            "articles": [
                                {
                                    "author": "Guilherme Dearo",
                                    "content": "São Paulo – Segundo uma pesquisa recente do Datafolha, saúde é a maior preocupação dos brasileiros, com 23% da população (quase um entre quatro) citando a questão como a mais importante da atualidade. Saúde superou segurança, que dominava a lista das maiores … [+13778 chars]",
                                    "description": "EXAME entrevistou especialistas na área de saúde para analisar a qualidade e viabilidade das propostas de Bolsonaro e Haddad",
                                    "publishedAt": "2018-10-21T09:00:05Z",
                                    "source": {
                                        "id": null,
                                        "name": "Abril.com.br"
                                    },
                                    "title": "O que propõem Haddad e Bolsonaro para a Saúde, maior preocupação nacional",
                                    "url": "https://exame.abril.com.br/brasil/o-que-propoem-haddad-e-bolsonaro-para-a-saude-maior-preocupacao-nacional/",
                                    "urlToImage": "https://abrilexame.files.wordpress.com/2016/09/size_960_16_9_protestos18.jpg?quality=70&strip=info&w=680&h=453&crop=1"
                                }
                            ],
                            "status": "ok",
                            "totalResults": 1
                        }"""
        # Extracts the articles from the results
        json_results = json.loads(raw_news)
        json_new = json_results['articles']
        # Creates the News instance
        news_new = MODELS.News.from_json(json_new[0])
        # Tests result
        self.assertEqual(MODELS.News, type(news_new))
        self.assertEqual("O que propõem Haddad e Bolsonaro para a Saúde, maior preocupação nacional", news_new.title)
        self.assertEqual("https://exame.abril.com.br/brasil/o-que-propoem-haddad-e-bolsonaro-para-a-saude-maior-preocupacao-nacional/", news_new.url)

# Runs tests when executing file
if __name__ == '__main__':
    unittest.main()