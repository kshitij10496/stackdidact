import random
import requests

from .question import Question
ids = []

def request_site(url, data):
    response = requests.get(url, data=data)
    return response.json()

def generate_question(url, data):
    """
    data : list of strings 
    """
    if not ids: 
        response = request_site(url, data)
        question_set = response["items"]
        question_body = random.choice(question_set)
        question_id = question_body["question_id"]

        for question in question_set:
            this_question_id = question["question_id"]
            if question_id != this_question_id:
                ids.append(this_question_id)
        
    else:
        question_id = random.choice(ids)

    question = Question.from_id(question_id)
    print(question.title)
 