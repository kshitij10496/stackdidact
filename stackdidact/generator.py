import random
import json

import requests
from colorama import Fore, Back, Style

from .question import Question
from .settings import URL, BASE_DIR

path = BASE_DIR + '/id_data.json'

try:
    with open(path, 'r') as fp:
        id_data = json.load(fp)

except FileNotFoundError:
    with open(path, 'w') as fp:
        id_data = {
                'yes': [],
                'no': []
        }
        json.dump(id_data, fp)

ids = id_data['yes'] # store the ids of the questions already displayed

def request_site(data):
    response = requests.get(URL, data=data)
    return response.json()

def format(question):
    print(Fore.CYAN + Style.BRIGHT + "Q: " + Fore.RED + Style.BRIGHT + question.title)
    print(Fore.YELLOW + "tags: " + ', '.join(question.tags))
    print(Fore.MAGENTA + "OP: " + question.owner_name)
    print(Fore.GREEN + "Read the discussion :" + question.link)

def generate_question(data):
    """
    data : list of strings 
    """
    temp_ids = get_ids(data)
    question_id = logic(temp_ids, data)
    temp_ids.remove(question_id)
    id_data['no'] += temp_ids
    with open(path, 'w') as fp:
        json.dump(id_data, fp)

    question = Question.from_id(question_id)
    format(question)
 
def get_ids(data):
    temp_ids = []
    response = request_site(data)
    question_set = response["items"]
    for question in question_set:
        temp_ids.append(question["question_id"])
    
    return temp_ids

def logic(temp_ids, data):
    """ Generate random question_id from list of ids.
    """
    question_id = random.choice(temp_ids)
    if not question_id in ids:
        ids.append(question_id)
        return question_id

    elif set(temp_ids) <= set(ids):
        # make another request
        if len(ids) >= data['page'] * data['pagesize']:
            data['page'] += 1

        new_temp_ids = get_ids(data) 
        return logic(new_temp_ids, data, URL)
    
    else:
        new_temp_ids = temp_ids.remove(question_id)
        return logic(new_temp_ids, data)
