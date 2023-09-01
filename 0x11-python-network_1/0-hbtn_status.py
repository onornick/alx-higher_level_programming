#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    utf8 = body.decode('utf-8')
    print('Body response:$')
    print(f"\t - type: {type(body)}$")
    print(f"\t - content: {body}$")
    print(f"\t - utf8 content: {utf8}$")
