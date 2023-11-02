import requests
from bs4 import BeautifulSoup
from os import environ

title_list = []

response = requests.get(environ['URL'])
print(response.raise_for_status())
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
titles = soup.find_all(name='h3', class_='title')
for title in titles:
    title = title.getText()
    title_list.append(title)
title_list.reverse()
print(type(title_list[0]))

with open('.\\movies.txt', 'w', encoding="utf-8") as movies:
    for t in title_list:
        movies.write(t + '\n')
