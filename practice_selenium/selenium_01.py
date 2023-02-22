#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import wordcloud 


#設定 Chrome Driver 的執行檔路徑
options=Options()
options.chrome_executable_path='/Users/timtsai/Documents/Jane/practice_selenium/chromedriver'
#建立 Driver 物件實體，用程式做瀏覽器運作
driver=webdriver.Chrome(options=options)
#連線到 PTT股票版
#取得股票版中的文章標題
def getData():
    driver.get('https://www.ptt.cc/bbs/Stock/index5930.html')
    tags = driver.find_elements(By.CLASS_NAME, 'title')  #搜尋 class 屬性是 title 的所有標籤
    for tag in tags:
        print(tag.text)

    #取得上一頁的文章標題
    link=driver.find_element(By.LINK_TEXT,'‹ 上頁')
    link.click() #模擬使用者點擊連結標籤
    tags = driver.find_elements(By.CLASS_NAME, 'title')  #搜尋 class 屬性是 title 的所有標籤
    for tag in tags:
        print(tag.text)
        with open("stock_title.txt",mode="a+",encoding="utf-8") as aa1:  ### w會複寫，建議改成a
            aa1.write(tag.text+"\n") ###+\n 是為了每個標題之間要換行

count=0
while count<80:
    getData()
    time.sleep(1)
    count+=1
driver.close()


content = open('stock_title.txt', 'rb').read()
jieba.load_userdict('./data0.csv') #使用自定義的檔案作為斷詞的優先依據
seg_list = jieba.lcut(content) #針對stock title為來源作斷詞,lcut是將返回型態變成list


dictionary = Counter(seg_list) #計算各斷詞的出現次數
STOP_WORDS = [' ', '，', '（', '）', '...', '。', '「', '」', '[', ']','情報','標的','新聞','\n',':','標','的','Re',"/",'TW','！','.','-','排行','第','於','01','02','03','04','05',
              '06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','112'
              ] #定義停用詞
[dictionary.pop(x, None) for x in STOP_WORDS] # 從字典裡刪除停用詞
print(dictionary) # 把計算完的每個分詞出現次數顯示出來看看


TC_FONT_PATH = 'NotoSansTC-Regular.otf' # 繁體中文字型檔名


# 文字雲格式設定
wc = wordcloud.WordCloud(background_color='white',
                         margin=2, # 文字間距
                         font_path=TC_FONT_PATH, # 設定字體
                         max_words=200, # 取多少文字在裡面
                         width=1280, height=720) # 解析度
                         
# 生成文字雲
wc.generate_from_frequencies(dictionary) # 吃入次數字典資料

# 產生圖檔
wc.to_file('WordCloud.png')

# 顯示文字雲圖片plt.imshow(wc)