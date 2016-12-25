from src.generator import generate_question

def main():
    data = {
        'page': 1,
        'pagesize': 10,
        'order' : 'desc',
        'sort': 'votes',
        'tagged': 'python',
        'site': 'stackoverflow'
        }
    url = 'https://api.stackexchange.com/2.2/questions'
    generate_question(url, data)

if __name__ == '__main__':
    main()
