import os

text = input('input text: ')
path = input('path: ')

def getfiles(path):
    f = 0
    os.chdir(path) #os.chdir 用於改變當前工作目錄到指定的路徑, path 為新的路徑  //os.getcwd 是獲得當下在運行 python 的路徑
    files = os.listdir() #os.listdir 用於回傳指定的文件夾的所有文件和文件夾之列表
    #print(filses)

    for file_name in files:
        abs_path = os.path.abspath(file_name) #abs_path 絕對路徑
        if os.path.isdir(abs_path): #判斷 abs_path 是否為目錄
            getfiles(abs_path) #若 True, 則執行getfiles
        if os.path.isfile(abs_path): #判斷 abs_path 是否為文件
            f = open(file_name, 'rt', encoding='utf-8',errors='ignore') #若 True, 則打開此文件, 並查找文件內的text
            if text in f.read(): #若 text 有在文件內
                f = 1 
                print(text + ' found in ')
                final_path = os.path.abspath(file_name)
                print(final_path)
                return True
            else: 
                f = 0

    if f == 0: 
        print(text +' not found! ')
        return False

getfiles(path)


#error: UnicodeDecodeError >> f = open(file_name, 'rt', encoding='utf-8',errors='ignore')
#FileNotFoundError >> 貼上完整的路徑
# not found 之情境? OK
#Q: 找出所有有出現 text 之文件


