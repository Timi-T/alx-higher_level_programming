#!/usr/bin/python3
"""
get my github handle
"""

if __name__ == "__main__":

    import requests
    import sys

    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/users/'
    try:
        my_profile = requests.get(url+username, auth=(username, token))
        my_info = my_profile.json()
        print(my_info['id'])
    except KeyError:
        print('None')
