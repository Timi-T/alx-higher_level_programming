#!/usr/bin/python3
"""
script to get status of a response
"""

if __name__ == "__main__":

    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    b = response.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(b), b))
