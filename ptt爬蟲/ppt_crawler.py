import requests
from bs4 import BeautifulSoup
#八卦版標題爬蟲
r = requests.Session() #Session會將你送出的requests所收到的cookies全部儲存起來並且在發送下一次請求時送出對應的參數。
payload={ #須送之參數
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
}
r1 = r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)
r2 = r.get("https://www.ptt.cc/bbs/Gossiping/index.html")
# print(r2.text)
soup = BeautifulSoup(r2.text,"html.parser")
sel = soup.select("div.title a")
for i in sel:
    print(i.text)
# r = requests.get("https://www.ptt.cc/bbs/index.html")
# soup = BeautifulSoup(r.text,"html.parser")
# sel = soup.select("div.board-title")
# print(sel)
# for i in sel:
#     print(i.text)