import random
import string

total = string.ascii_letters + string.digits + string.punctuation #total = ascii 內字母＋數字＋標點之組合

length = 16

password = "".join(random.sample(total, length)) # random.sample: 從 total 中隨機取指定數量的字元

print(password)