#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        res = res.json()
        if len(res) == 0:
            print('No result')
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
