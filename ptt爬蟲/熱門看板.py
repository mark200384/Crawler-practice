import requests
from bs4 import BeautifulSoup
import re


def replace_all_blank(value):
    result = re.sub('\W+', '', value).replace("_", '')
    # print(result)
    return result


url = "https://www.ptt.cc/bbs/hotboards.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
boardNames = []
popularities = []
titles = []
boardNameElements = soup.find_all('div', class_="board-name")
popularityElements = soup.find_all('div', class_="board-nuser")
boardTitleElements = soup.find_all('div', class_="board-title")
# print(boardNameElements)
# print(popularityElements)
# print(boardTitleElements)
for t in boardNameElements:
    boardNames.append(t.text)
# print(boardNames)
for e in popularityElements:
    popularities.append(e.text)
# print(popularities)
for t in boardTitleElements:
    temp = replace_all_blank(t.text)
    titles.append(temp)

for pop, bn, ti in zip(popularities, boardNames, titles):
    print(pop, bn, ti)

import csv

with open('ptt_hot.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['種類', '人氣 ', '標題'])
    for i in range(len(titles)):
        writer.writerow([boardNames[i], popularities[i], titles[i]])
