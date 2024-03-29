#!/usr/bin/python3
""" a Python script that takes your GitHub credentials (username
    and password)
    and uses the GitHub API to display your id
    You must use Basic Authentication with a personal access token
    as password to access to your information
    (only read:user permission is needed)
    The first argument will be your username
    The second argument will be your password (in your case,
    a personal access token as password)
    You must use the package requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./file.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    Auth = {"Authorization": f"token {password}"}

    response = requests.get(url, headers=Auth)
    if response.status_code == 200:
        user_info = response.json()
        print(f"{user_info.get('id')}")
    else:
        print('None')
