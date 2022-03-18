#!/usr/bin/python3
"""
send a request to a url
"""

import sys
from urllib.request import urlopen
import json


url = sys.argv[1]
with urlopen(url) as response:
    pass
print(response.headers['X-Request-Id'])
