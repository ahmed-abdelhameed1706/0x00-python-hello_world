#!/usr/bin/python3
"""
script to send email to a url
"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {
            "email": email
            }
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as html:
        response = html.read()

    print(response.decode('utf-8'))
