import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)

soup = BeautifulSoup(r.text, features="html.parser")

atags = soup.find_all('a')

with open('file_to_save.txt', 'wb') as open_file:
    for a in atags:
        s = str(a.contents) + ": "  + str(a['href'])
        open_file.write(s.encode("utf-8"))