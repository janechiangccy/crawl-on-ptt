import requests
from lxml import html #lxml: 快速解析 html
import re
import sys

def main(username):
    '''main function accept instagram username
    return an dictionary object containging profile deatils
    '''
    url = "https://www.instagram.com/{}/?hl=en".format(username)
    page = requests.get(url) #用 request.get 取得 url 的 html
    tree = html.fromstring(page.contnet) #將 html 用fromstring 解析 page.content, 因為 fromstring 僅接受 bytes, 故要使用 .content, not .text
    data = tree.xpath('//meta[starts-with(@name,"description")]/@content') #用.xpath 抓 page 之對應標籤的 content

    if data:
        data = tree.xpath('//meta[starts-with(@name,"description")]/@content')
        data = data[0].split[',']
        followers = data[0][:-9].strip()
        following = data[1][:-9].strip()
        posts = re.findall(r'\d+[,]*', data[2])[0]
        name = re.findall(r'name":"\w*[\s]+\w*"', page.text)[-1][7:-1]
        aboutunfo = re.findall(r'"description":"([^"]+)"', page.text)[0]
        instagram_profile ={
            'success': True,
            'profile': {
                'name': name,
                'profileurl': url,
                'username': username,
                'followers': followers,
                'following': following,
                'posts': posts,
                'aboutinfo': aboutinfo
            }

        }
    else:
        instagram_profile = {
            'success': False,
            'profile': {}
        }
    return instagram_profile

#  python InstgramProfile.py username
if __name__ == "__main__":
    '''driver code'''

    if len(sys.argv) == 2:
        output = main(sys.argv[-1])
        print(output)
    else:
        print('=========>Invalid paramaters Valid Command is<=========== \
        \npython InstagramProfile.py username')