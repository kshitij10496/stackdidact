import click
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

    def __str__(self):
        title = "Q: " + self.title
        tags = "tags: " + ', '.join(self.tags)
        owner_name = "OP: " + self.owner_name
        link = "Read the discussion :" + self.link
        return "\n".join([title, tags, owner_name, link])

    def color_format(self):
        colored_title = click.style("Q: ", fg='cyan', bold=True) + \
                        click.style(self.title, fg='red', bold=True)
        colored_tags = click.style("tags: " + ', '.join(self.tags), fg='yellow')
        colored_owner_name = click.style("OP: " + self.owner_name, fg='magenta')
        colored_link = click.style("Read the discussion: " + self.link, fg='green')
        return "\n".join([colored_title, colored_tags, colored_owner_name, colored_link])

    @classmethod
    def from_id(cls, question_id):
        main_url = URL + '/' + str(question_id)
        data = {
            'site': SITE,
            }
        response = requests.get(main_url, data=data).json()
        question_body = response['items'][0]
        tags = html.unescape(question_body["tags"])
        owner_name = html.unescape(question_body["owner"]["display_name"])
        title = html.unescape(question_body["title"])
        link = html.unescape(question_body["link"])
        return cls(tags, owner_name, question_id, title, link)
