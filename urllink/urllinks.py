# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
pos = raw_input('Position - ')
time = raw_input('Time - ')
pos = int(pos)
time = int(time)


# Retrieve all of the anchor tags
while time > 1:
    time = time - 1
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    cnt = 0
    for tag in tags:
        st = tag.get('href', None)
        cnt = cnt + 1
        if cnt == pos:
            url = st
            break
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
print tags[pos-1]
        