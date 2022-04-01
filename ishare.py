import sys
import requests

SERVER = "http://i-share.top"

def help():
    helpString = '\n    Usage ishare [action] [param]\n\n    action:\n        search  :   Search images\n       detail  :   Detail information of image\n        help    :   Show this help page\n\n    Example\n    - ishare search vios\n    - ishare detail vios-3.4.5\n    '
    print(helpString)

def getInfo(name):
    result = requests.get(SERVER + '/api/user/ishare/detail?name=' + name).json()
    if not result['result']:
        print(result['message'])

    x = result['data']
    print(x)

def search(search):
    result = requests.get(SERVER + '/api/user/ishare/search?search=' + search).json()
    if not result['result']:
        print(result['message'])

    for x in result['data']:
        print(x)

def main():
    argvs = sys.argv
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        help()
        return
    action = argvs[1]
    if action == 'search':
        searchData = argvs[2]
        search(searchData)
    if action == 'detail':
        name = argvs[2]
        getInfo(name)

if __name__ == '__main__':
    main()