#!/usr/bin/python3
"""list 10 commits
"""
import requests
from sys import argv


import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    req = requests.get(url)
    commits = req.json()
    try:
        for c in range(10):
            sha = commits[c].get("sha")
            name = commits[c].get("commit").get("author").get("name")
            print("{}: {}".format(commits[c].get(sha, name)))
    except IndexError:
        pass
