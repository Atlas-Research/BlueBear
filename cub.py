import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
#import datetime
#from datetime import date
#from bs4 import BeautifulSoup

#url = "https://simple.wikipedia.org/wiki/List_of_countries"

#res = requests.get(url)
#soup = BeautifulSoup(res.text,"lxml")
#for items in soup.find(class_="wikitable").find_all("tr")[1:]:
    #data = items.find("td").get_text(strip=True)
    #print(data)
symbol = ''
#start_date = datetime.datetime(2017, 12, 1)
#end_date = datetime.datetime(2017, 12, 31)

start = '2019, 01, 01'
end = '2019, 01, 14'
google = pdr.DataReader(symbol, 'stooq', start, end)
print('This Tick Data')
print("------\n")
print(google.head())
print("------\n")
google_close = pd.DataFrame(google.Close)
print('This is Close', google_close.last_valid_index)
google_close['MA_9'] = google_close.Close.rolling(9).mean()
google_close['MA_20'] = google_close.Close.rolling(20).mean()
google_close['MA_200'] = google_close.Close.rolling(200).mean()
#google_close['MA_60'] = google_close.Close.rolling(60).mean()
##print(google_close.Close)
plt.figure(figsize=(15, 10))
plt.grid(True)

#display MA's
plt.plot(google_close['Close'], label='')
plt.plot(google_close['MA_9'], label='MA 9 day')
plt.plot(google_close['MA_20'], label='MA 20 day')
plt.plot(google_close['MA_200'], label='MA 200 day')
#plt.plot(google_close['MA_60'], label='MA 60 day')
plt.legend(loc=3)
plt.show()
pdr.show()
#pdr.close()
pdr.close.head(10)