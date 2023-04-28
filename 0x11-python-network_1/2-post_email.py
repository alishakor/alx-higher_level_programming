#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST
    request to the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if _name_ == "_main_":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as feedback:
        print(feedback.read().decode('utf-8'))
