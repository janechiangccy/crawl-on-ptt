import os
from PIL import Image

def watermark_photo(input_image_path,watermark_image_path,output_image_path):
    base_image = Image.open(input_image_path) #base_image 為input 之圖檔路徑
    watermark = Image.open(watermark_image_path).convert("RGBA")
    # add watermark to your image
    position = base_image.size #用 PIL 內取得 .size 資訊
    newsize = (int(position[0]*8/100),int(position[0]*8/100)) # watermark 的尺寸, position[0]= original width, position[1]= length
    print(position)
    watermark = watermark.resize(newsize)
    # return watermark
    print(newsize)
   
    #print(position[0], position[1], newsize[0], newsize[1])

    new_position = position[0]-newsize[0]-20,position[1]-newsize[1]-20 # watermark 要放的位置
    # create a new transparent image
    transparent = Image.new(mode='RGBA',size=position,color=(0,0,0,0))
    # paste the original image
    transparent.paste(base_image,(0,0)) #在 transparent 貼上 base_image 
    # paste the watermark image


    #???????>>要mask的圖, paster & mask 哪裡不同
    transparent.paste(watermark,new_position,watermark) #first watermark >>要貼的圖, second watermark 
    
    
    image_mode = base_image.mode
    print(image_mode)
    if image_mode == 'RGB':
        transparent = transparent.convert(image_mode)
    else:
        transparent = transparent.convert('P') #pixel
    transparent.save(output_image_path,optimize=True,quality=100) # .save: 儲存圖檔
    print("Saving"+output_image_path+"...")

folder = input("Enter Folder Path: ")
watermark = input("Enter Watermark Path: ")
os.chdir(folder)
files = os.listdir(os.getcwd())
print(files)

if not os.path.isdir("output"): #建立一個 output 的 folder
    os.mkdir("output")

c = 1
for f in files:
    if os.path.isfile(os.path.abspath(f)):
        if f.endswith(".png") or f.endswith(".jpg"):
            watermark_photo(f,watermark,"output/"+f)


#watermark 變形, 做成透明的浮水印 >> 將watermark 轉成 png?
