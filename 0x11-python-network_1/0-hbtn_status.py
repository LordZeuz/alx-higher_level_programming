#!/usr/bin/python3
"""A script to fetch https://alx-intranet.hbtn.io/status"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    feedback = response.read()

print("Body response:")
print("\t- type: {}".format(type(feedback)))
print("\t- content: {}".format(feedback))
print("\t- utf8 content: {}".format(feedback.decode('utf-8')))
