URL = 'https://api.stackexchange.com/2.2/questions'
SITE = 'stackoverflow'

LANG_TAGS = {
	'c': 'c',
	'py': 'python',
	'java': 'java',
	'hs': 'haskell',
	'rb': 'ruby',
	'rs': 'rust'
}

 # If a second arg is provided, this options will used to open the question in browser
USER_AGENT = {
'fox':'firefox',
'ggl': 'chromium'
}

DATA = {
        'page': 1,
        'pagesize': 30, # mentioning the default value for completeness
        'order' : 'desc',
        'sort': 'votes',
        'tagged': 'python', # Searches for questions using this tag; searches for python questions by default
        'site': SITE # search website in the Stack Exchange family
    }
