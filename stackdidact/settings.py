import os

# Set a predefined list of browser if the user hasn't defined them already
predefined_agents = os.pathsep.join(['firefox','google-chrome', 'lynx', 'w3m', 'opera', 'macosx', 'safari'])
_ = os.environ.setdefault('BROWSER', predefined_agents)

URL = 'https://api.stackexchange.com/2.2/questions'
SITE = 'stackoverflow'
DEFAULT_TAG = 'python'

QUERY_PARAMS = {
        'page': 1,
        'pagesize': 30,  # mentioning the default value for completeness
        'order': 'desc',
        'sort': 'votes',
        'tagged': DEFAULT_TAG,
        'site': SITE # search website in the Stack Exchange family
    }
PATH = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.split(PATH)[0]
