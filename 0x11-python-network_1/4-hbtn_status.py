#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""
from requests import get


if __name__ == '__main__':
    url = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    dec = url.content.decode('utf-8')
    print("\t- content: {}".format(dec))
