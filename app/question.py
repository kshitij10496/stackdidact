import html

import requests

from .settings import URL, SITE

class Question:

    def __init__(self, tags, owner_name, question_id, title, link):
        self.tags = tags
        self.owner_name = owner_name
        self.question_id = question_id
        self.title = title
        self.link = link

    @classmethod
    def from_id(cls, question_id):
        main_url = URL + '/' + str(question_id)
        data = {
            'site' : SITE,
            }
        response = requests.get(main_url, data=data).json()
        question_body = response['items'][0]
        tags = html.unescape(question_body["tags"])
        owner_name = html.unescape(question_body["owner"]["display_name"])
        title = html.unescape(question_body["title"])
        link = html.unescape(question_body["link"])
        return cls(tags, owner_name, question_id, title, link)
