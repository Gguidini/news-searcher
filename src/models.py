"""
This module defines the classes used in the system.
"""

class News:
    """
    Defines a News object.
    News are retrieved using NewsAPI (https://newsapi.org/)
    """

    def __init__(self, source, author, title, description, url, url_to_image, published_at, content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content = content
        self.score = 0

    def __str__(self):
        return self.title

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __eq__(self, other):
        return self.score == other.score

    def __ge__(self, other):
        return self.score >= other.score

    def set_score(self, score):
        """
        Defines the score for a News, after it's calculated.
        """
        self.score = score
