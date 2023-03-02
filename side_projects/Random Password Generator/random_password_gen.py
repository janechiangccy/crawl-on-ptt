import random
import math

#定義 password 內可使用之符號
alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
special = '+-*/'


pass_len = int(input('Enter Password Length: '))
alpha_len = pass_len//2 #字母取 pass_len/2 之整數長度
num_len = math.ceil(pass_len*30/100) #num 取 pass_len 之30%的ceilling
special_len=pass_len-(alpha_len+num_len)

password = [] #定義 password 之型態

#用函數包裝 password 產生器
def generate_pass(length, array, is_alpha = False): # 若 index 之對應為 alpha, 則進入 if 判斷要取大/小寫
    for i in range(length):
        index = random.randint(0, len(array)-1)
        character = array[index] # character 為array[indext] 的其中一個字
        if is_alpha:
                case = random.randint(0, 1)
                if case == 1:
                    character = character.upper()
        password.append(character) #將 character append 至 password 的 array 內


generate_pass(alpha_len, alpha, True)
generate_pass(num_len, num)
generate_pass(special_len, special)
random.shuffle(password) #打亂 password 的次序
gen_password = "" #將 password 用 str 的方式串在一起
for i in password:
        gen_password = gen_password +str(i)
print(gen_password)