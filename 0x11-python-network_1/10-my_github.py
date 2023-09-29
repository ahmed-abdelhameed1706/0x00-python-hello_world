#!/usr/bin/python3
"""
script to get my id from github
"""


import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]

    url = f"https://api.github.com/users/{user}"

    headers = {"Authorization": f"token {pw}"}

    r = requests.get(url, headers=headers).json()

    print(r.get("id"))
