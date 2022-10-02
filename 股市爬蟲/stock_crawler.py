import requests
from bs4 import BeautifulSoup

r = requests.get("https://query1.finance.yahoo.com/v7/finance/download/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&crumb=hP2rOschxO0")
# soup = BeautifulSoup(r.text,"html.parser")
# print(soup)

import pandas as pd
from io import StringIO
p = pd.read_csv(StringIO(r.text))
print(p)