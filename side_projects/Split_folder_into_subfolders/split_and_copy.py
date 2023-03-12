import glob  # glob 類似於文件搜尋功能, 找出匹配條件之檔案或是資料夾
import os
from shutil import copy2  # shutil 提供對文件和文件集合進行高階操作，如 copy, delete...
import sys

def get_files(path):
    '''
    return a list of files available in given folder
    '''
    files = glob.glob(f'{path}/*')  #抓取 path 內之所有文件(/*)  #???? what is f'{path}'/* means?
    return files

def getfullpath(path):
    '''
    return absolute path of given file
    '''
    return os.path.abspath(path)

def copyfiles(src, dst):  # dst 須為完整的文件名稱，否則會引發 SameFileError
    '''
    This function copy file from src to dst
    if dst dir is not there it will create new
    '''
    if not os.path.isdir(dst):
        os.makedirs(dst)
    copy2(src, dst)  # copy, copy2 之差別在於 copy2 會保留原文件之資料

def split(data, count):
    '''
    Split Given list of files and return generator
    '''
    for i in range(1, len(data), count): # range(start, stop, step), step 默認為1
        if i + count-1 > len(data):
            start, end = (i-1, len(data))
        else:
            start, end = (i-1, i+count-1)
        yield data[start:end]  # 用 generator 儲存資料，以節省記憶體空間


def start_process(path, count):
    files = get_files(path)
    splited_data = split(files, count)

    for idx, folder in enumerate(splited_data):  # enumerate 迴圈的計數器, idx: index
        name = f'data_{idx}'
        for file in folder:
            copyfiles(getfullpath(file), getfullpath(name))


if __name__ == '__main__':
    '''
    drive code
    To run this script
    python split_and_copy.py <input folder path> <20>
    '''
    if len(sys.argv) != 3:  # sys.argv 取得執行 python 檔案時命令列參數的方法 #??????
        print('Please provide correct parameters \
        \n python spilt_and_copy.py <input folder path> <count>')
        sys.exit(0)

    if len(sys.argv) == 3:
        path = sys.argv[1]  # path = 命令列的第[1]個 input
        if os.path.isdir(path):
            count = sys.argv[2]
            start_process(path, int(count))
        else:
            print('Given directory name is not an valid directiry')
    else:
        print('Wrong parameter are provide')


# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         print('no argument')
#         sys.exit()
#     print(len(sys.argv))
#     print(sys.argv[0])
#     print(sys.argv[1])

# two Qs in line 10, 56



