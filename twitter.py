import re
url=input("url: ")
k=re.match('^https://x.com/(\w.+)',url)
if k:
    print(k.group(1))



