#!/usr/bin/python3
"""
get last 10 commits of a github user
"""

if __name__ == "__main__":

    import sys
    import requests

    repo = sys.argv[1]
    username = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(username, repo)
    response = requests.get(url)
    my_info = response.json()
    try:
        i = 0
        while i < 10:
            sha = (my_info[i])['sha']
            name = (my_info[i])['commit']
            name = name['author']
            name = name['name']
            print("{}: {}".format(sha, name))
            i += 1
    except IndexError:
        pass
