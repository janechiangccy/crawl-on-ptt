import os
import sys
import collections
import string

script_name = sys.argv[0]

res = {
    "total_lines":"",
    "total_characters":"",
    "total_words":"",
    "unique_words":"",
    "special_characters":""
}


try:
    textfile = sys.argv[1]
    with open(textfile, "r", encoding = "utf-8") as f:

        data = f.read()
        res["total_lines"] = data.count(os.linesep) #計算行終止符的個數 linesep: 行終止符(\n)
        res["total_characters"] = len(data.replace(" ","")) - res["total_lines"] #計算單字個數
        counter = collections.Counter(data.split()) # data.split 分割單字, 並用 collections.Counter 來裝個單字之出現次數. Counter 所生成之型態為 dict 的子類別
        d = counter.most_common()   # d 為統計所有元素對應之出現次數
        print(d)
        res["total_words"] = sum([i[1] for i in d]) # i[1] 表示 d 內對應單字之次數為何, 將其進行加總, 即可算出 total_words 
        res["unique_words"] = len([i[1] for i in d]) #計算 i[1] 內之元素個素
        special_chars = string.punctuation  # string.punctiation 所有的標點符號
        res["special_characters"] = sum(v for k, v in collections.Counter(data).items() if k in special_chars)  #加總所有在 v 所對應的 key 為 special_chars

except IndexError:
    print('Usage: %s TEXTFILE' % script_name)
except IOError:
    print('"%s" cannot be opened.' % textfile)

print(res)
