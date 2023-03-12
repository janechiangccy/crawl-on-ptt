from tqdm import tqdm
from PIL import Image
import os
from time import sleep

#定義可調整圖像尺寸之函數
def Resize_image(size, image):  
    if os.path.isfile(image):
        try:
            im = Image.open(image)
            im.thumbnail(size, Image.ANTIALIAS) #im.thumbnail: 製作縮圖, Image.ANTIALIAS: 對 image 進行平滑濾波的處理
            im.save('resize/'+ str(image) + ".jpg") #儲存 image
        except Exception as ex:
            print(f'Error: {str(ex)} to {image}')

path = input('Enter Path to images: ')
size = input('Size Height, Width: ')
size = tuple(map(int, size.split(","))) #?????? tuple, map 之使用情境

os.chdir(path)

list_images = os.listdir(path)  #建立 path 內之文件之 list
if 'resize' not in list_images: #新增 resize 資料夾
    os.madir('resize')

for image in tqdm(list_images, desc='Resizing Images'): #desc(description): 進度條旁的備註說明
    Resize_image(size, image)
    sleep(0.1)  #讓程式暫停0.1秒
print('Resizing Complete!')

