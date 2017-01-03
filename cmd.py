import webbrowser
import sys
from stackdidact.generator import generate_question
from stackdidact.settings import DATA, LANG_TAGS

def main():
    args = sys.argv[1:]
    lang = LANG_TAGS.get(args[0])
    if lang:
        DATA['tagged'] = lang
    generate_question(DATA, args[1])

if __name__ == '__main__':
    main()
