#!/usr/bin/python3
"""
post request with search letter
"""

if __name__ == "__main__":

    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""
    response = requests.post(url, params={'q': letter})
    try:
        if response.json():
            resp_id = response.json().get('id')
            resp_name = response.json().get('name')
            print("[{}] {}".format(resp_id, resp_name))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
