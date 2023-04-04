#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":

    url = sys.argv[1]

    req = urllib.request.Request(url)
    response = urllib.request.urlopen(url)
    feedback = response.headers
    print(feedback.get('X-Request-ID'))
