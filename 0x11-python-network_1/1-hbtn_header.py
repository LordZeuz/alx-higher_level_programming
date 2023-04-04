#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        feedback = response.headers
    print(feedback.get('X-Request-ID'))
