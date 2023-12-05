#!/usr/bin/python3
"""
sends a post request to the passed URL with email
"""
import sys
import requests


if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], values)
    print(r.text)
