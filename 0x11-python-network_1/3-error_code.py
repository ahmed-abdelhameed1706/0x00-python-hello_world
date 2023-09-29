#!/usr/bin/python3
"""
script to send request and print response and catch errors
"""


import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as html:
            response = html.read()
            print(response.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
