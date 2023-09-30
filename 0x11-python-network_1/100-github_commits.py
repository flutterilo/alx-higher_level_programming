#!/usr/bin/python3
"""
    Authenticated into github Api using basic authentication 
    and retrieve user id.
"""
import requests
from sys import argv


if __name__ == "__main__":
    repo, username = argv[1:]
    url = f"https://api.github.com/repos/{username}/{repo}/commits?per_page=10&sort=committer-date"
    r = requests.get(url, auth=(
        username, "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"))
    try:
        for item in r.json():
            print(
                f"{item['sha']} {item['commit']['author']['name']}")
    except Exception as e:
        print(e)
        pass
