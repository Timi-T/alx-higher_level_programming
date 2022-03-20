#!/usr/bin/python3
"""
http error handling
"""

if __name__ == "__main__":

    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys

    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            body = response.read()
        print(body)
    except HTTPError as e:
        print(e.code)
        print("Error code: {}".format(e.code))
