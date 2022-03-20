#!/usr/bin/python3
"""
post request with search letter
"""

if __name__ == "__main__":

    import requests
    import sys

    url = "https://httpbin.org/post"
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""
    response = requests.post(url, params={'q': letter})
    info = response.content
    print(info)
