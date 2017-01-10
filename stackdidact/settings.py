import os

import requests

URL = 'https://api.stackexchange.com/2.2/questions'
SITE = 'stackoverflow'
TAG = 'python'
DATA = {
        'page': 1,
        'pagesize': 30,  # mentioning the default value for completeness
        'order': 'desc',
        'sort': 'votes',
        'tagged': TAG,  # Searches for questions using this tag
        'site': SITE  # search website in the Stack Exchange family
    }

def get_all_sites():
    all_sites = {}
    r = requests.get('https://api.stackexchange.com/2.2/sites', {"pagesize": 400})
    for item in r.json()["items"]:
        all_sites[item["api_site_parameter"]] = item["name"]

    return all_sites

ALL_SITES = get_all_sites()
