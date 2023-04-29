#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to solve
this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests
and sys
You don’t need to check arguments passed to the script
(number or type)"""


import sys
import requests

if _name_ == "_main_":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r = requests.get(url)
    for commit in r.json()[:10]:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
