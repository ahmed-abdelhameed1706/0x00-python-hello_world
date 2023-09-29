#!/usr/bin/python3
"""
script to search user
"""


import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"

    q = ''

    if letter:
        q = letter

    data = {"q": q}

    r = requests.post(url, data=data)

    try:
        if r.json():
            if 'id' in r.json() and "name" in r.json():
                print(f"[{r.json()['id']}] {r.json()['name']}")
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
