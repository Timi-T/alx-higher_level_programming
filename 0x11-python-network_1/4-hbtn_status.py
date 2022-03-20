#!/usr/bin/python3
"""
script to get status of a response
"""

if __name__ == "__main__":

    from urllib.request import urlopen

    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        b = response.read().decode('utf-8')
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(b), b))
