import os

URL = 'https://api.stackexchange.com/2.2/questions'
SITE = 'stackoverflow'
DEFAULT_TAG = 'python'

# This is consulted for opening the question in user's browser
USER_AGENT = 'firefox'

QUERY_PARAMS = {
        'page': 1,
        'pagesize': 30,  # mentioning the default value for completeness
        'order': 'desc',
        'sort': 'votes',
        'tagged': DEFAULT_TAG, # Searches for questions using this tag; searches for python questions by default
        'site': SITE # search website in the Stack Exchange family
    }
PATH = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.split(PATH)[0]
