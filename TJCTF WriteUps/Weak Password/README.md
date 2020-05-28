---
title: 'Weak Password - WEB[ 50 ]'
created: '2020-05-28T11:45:30.256Z'
modified: '2020-05-28T11:52:54.626Z'
---

# Weak Password - WEB[ 50 ]

It seems your login bypass skills are now famous! One of my friends has given you a challenge: figure out his password on this site. He's told me that his username is admin, and that his password is made of up only lowercase letters and numbers. (Wrap the password with tjctf{...})

### Solution

It was a blind SQLi challenge where if you logged in you'll get the output as   `Congratulations` and if not you'll get an error.

We can easily log in with username as `admin` and password as `admin' or '1'='1'`.

But this won't give us the password so we attach another command in password field.
password : `admin' or '1'='1' and password like 'a%`

NOTE : The `%` sign in SQL is for any characters of any length follwing the given characters before it. 

This will check if the password starts with `a` and if it does we'll successfully login. So now we can just loop through the letters and get the values at each place.

