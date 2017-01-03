import os

URL = 'https://api.stackexchange.com/2.2/questions'
SITE = 'stackoverflow'
TAG = 'python'
DATA = {
        'page': 1,
        'pagesize': 30, # mentioning the default value for completeness
        'order' : 'desc',
        'sort': 'votes',
        'tagged': TAG, # Searches for questions using this tag
        'site': SITE # search website in the Stack Exchange family
    }
PATH = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.split(PATH)[0]