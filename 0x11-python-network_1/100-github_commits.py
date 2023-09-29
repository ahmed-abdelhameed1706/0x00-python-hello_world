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

    
    params = {"per_page": 10}

    r = requests.get(url, params=params)

    commits = r.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha} {author_name}")
        #print(f"{commit['sha']} {commit['commit']['author']['name']}")
