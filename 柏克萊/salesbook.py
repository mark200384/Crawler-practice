import requests
from bs4 import BeautifulSoup

url = "https://www.books.com.tw/web/sys_saletopb/books/01/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
sel = soup.select("div.type02_bd-a a")
# print(sel)
name = []
writer =[]
book =[]
info = []
URL = []
for s in sel:
    name.append(s.text)
    URL.append(s['href'])
for i in range(0,200):
    if i % 2==0:
        book.append(name[i])
    else:
        writer.append(name[i])
print(book)
print(name)
temp = ""
for i in range(101):
    temp = URL[i]
    if (temp[0] == '/' and temp[1] == '/'):
        URL.remove(temp)
print(len(URL))
sel = soup.select("div.type02_bd-a")
for s in sel:
    info.append(s.text)
# print(writer)
import pandas as pd
for i in range(len(info)):
    info[i].strip()
dic = {"Book": book,
       "info": info,
       "URL": URL}
data = pd.DataFrame(dic)
print(data)
data.to_csv("test.csv",index=True,encoding="cp950")