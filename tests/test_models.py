"""
Test cases for the News class.
"""
import unittest
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

# Runs tests when executing file
if __name__ == '__main__':
    unittest.main()