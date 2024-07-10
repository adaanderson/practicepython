import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r.text)
head_tag = soup.head
title_tag = head_tag.contents[0]

#print(soup.find("title"))
#title = soup.title.parent.name
#for link in 
print(soup.find_all('h1', 'h2', 'h3'))
tag = soup.h2
name = tag.name
#print(name)
    #print(tag)
atags = soup.find_all('a')

#title_tag = atags.content

for a in atags:
    print(str(a.contents[0]) + ": "  + str(a['href']))

#title1 = titles..find("href")

#print(titles)
#print(title1)