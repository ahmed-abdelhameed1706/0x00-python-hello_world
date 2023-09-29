#!/usr/bin/python3
"""
script to get a value from header of a url using requests
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r_headers = requests.get(url).headers

    print(r_headers['X-Request-Id'])
