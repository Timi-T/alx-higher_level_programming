#!/usr/bin/python3
"""
send a request to a url
"""

from urllib.request import urlopen
import json


with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
print('Body response:\n    - type: {}\n    - content: {}\n    - utf8 content:\
      {}'.format(type(body), body, body.decode('utf-8')))
