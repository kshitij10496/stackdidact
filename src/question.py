import requests
url = 'https://api.stackexchange.com/2.2/questions'
site = 'stackoverflow'

def request_site(url, data):
    response = requests.get(url, data=data)
    return response

class Question:

    def __init__(self, tags, owner_name, question_id, title, link):
        self.tags = tags
        self.owner_name = owner_name
        self.question_id = question_id
        self.title = title
        self.link = link

    @classmethod
    def from_id(cls, question_id):
        url = 'https://api.stackexchange.com/2.2/questions'
        main_url = url + '/' + str(question_id)
        data = {
            'site' : 'stackoverflow',
            }
        response = request_site(main_url, data)
        question_body = response.json()['items'][0]
        tags = question_body["tags"]
        owner_name = question_body["owner"]["display_name"]
        title = question_body["title"]
        link = question_body["link"]
        return cls(tags, owner_name, question_id, title, link)
