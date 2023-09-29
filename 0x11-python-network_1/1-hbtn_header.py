#!/usr/bin/python3
"""
script to get a value from header of a url
"""


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as html:
        request_headers = html.info()
        request_id = request_headers['X-Request-Id']

    print(request_id)
