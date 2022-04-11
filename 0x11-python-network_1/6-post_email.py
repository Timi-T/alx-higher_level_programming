#!/usr/bin/python3
"""
post to a url using requests library
"""

if __name__ == "__main__":

    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    my_data = {'email': email}
    response = requests.post(url, data=my_data)
    print(response.text)
