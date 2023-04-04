#!/usr/bin/python3
"""A script to fetch https://alx-intranet.hbtn.io/status"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    feedback = response.read()
