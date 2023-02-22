import requests
import pandas as pd

result = requests.get("https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market=1&issuetype=1&industry_code=&Page=1&chklike=Y")
df1 = pd.read_html(result.text)[0][2][1:]
filename = f'./data1.csv' #指定Data Frame轉存csv檔案的檔名與路徑
df1.to_csv(filename) #將Data Frame轉存為csv檔案
df2 = pd.read_html(result.text)[0][3][1:]
filename = f'./data2.csv' #指定Data Frame轉存csv檔案的檔名與路徑
df2.to_csv(filename) #將Data Frame轉存為csv檔案
print(df1, df2)

