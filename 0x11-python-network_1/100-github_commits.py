#!/usr/bin/python3
"""
the challenge script of holbertonschools
"""


import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"

    r = requests.get(url)

    commits = r.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
