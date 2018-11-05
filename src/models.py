"""
This module defines the classes used in the system.
"""

import json
from datetime import datetime

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
        self.date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        self.disease = ""
        self.region = ""
        self.country = "" 

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

    def to_json(self):
        """
        Transforms a News instance into a json object
        """
        dictionary = {
            'source' : self.source,
            'author' : self.author,
            'title' : self.title,
            'description' : self.description,
            'url' : self.url,
            'url_to_image' : self.url_to_image,
            'published_at' : self.published_at,
            'content' : self.content,
            'score' : self.score,
            'date' : self.date,
            'disease' : self.disease,
            'region' : self.region,
            'country' : self.country
        }
        return json.dumps(dictionary)

    @classmethod
    def from_json(cls, json):
        """
        Creates and returns a News instance from a json object.
        """

        return cls(json['source']['name'],
                   json['author'],
                   json['title'],
                   json['description'],
                   json['url'],
                   json['urlToImage'],
                   json['publishedAt'],
                   json['content'])


