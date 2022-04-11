#!/usr/bin/python3
"""
use requests module to get header value
"""

if __name__ == "__main__":

    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    try:
        print(response.headers['X-Request-Id'])
    except KeyError:
        pass
