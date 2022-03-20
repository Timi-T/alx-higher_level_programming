#!/usr/bin/python3
"""
use requests library to send a request to a url
"""

if __name__ == "__main__":

    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    code = response.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)
