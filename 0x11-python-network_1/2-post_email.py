#!/usr/bin/python3
"""
send a request to a url
"""
if __name__ == "__main__":
    import sys
    from urllib import parse, request
    import json

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    data = parse.urlencode(data).encode('ascii')
    with request.urlopen(url, data) as c:
        content = c.read().decode('utf-8')
    print(content)
