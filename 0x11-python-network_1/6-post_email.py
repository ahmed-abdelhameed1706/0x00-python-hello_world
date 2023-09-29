#!/usr/bin/python3
"""
script to send email to a url using requests
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {
            "email": email
            }
    r = requests.post(url, data).text

    print(r)
