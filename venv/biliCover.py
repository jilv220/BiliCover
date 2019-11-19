import json
import os
import requests
import urllib
import urllib3

mid = input('请输入空间号 : ')
pn = input('请输入页数 : ')
ps = input('请输入件数 : ')
folder = input("请输入要保存的文件夹名 : ")

# 空间 - 视频 url
url = 'https://api.bilibili.com/x/space/arc/search?mid=' + mid + '&ps=' + ps + \
      '&tid=0&pn=' + pn + '&keyword=&order=pubdate&jsonp=jsonp'

# init response
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
            'Referer': 'https://www.bilibili.com'}
urllib3.disable_warnings()  #从urllib3中消除警告
response = requests.get(url, headers=headers, verify=False)  #证书验证设为FALSE
content = json.loads(response.text)

#  用urllib下载图片
def urllib_download(file_path, img_name, img_url):
    try:
        # 是否有这个路径
        if not os.path.exists(file_path):
            # 创建路径
            os.makedirs(file_path)
        # 拼接图片名（包含路径）
        filename = os.path.normpath(file_path + '/' + img_name)
        print("图片已保存到 : " + filename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filename=filename)

    except IOError as e:
        print("IOError")

status_code = content.get('code')
if status_code == 0:

    for num in range(0,int(ps)):
        coverUrl = 'https:' + content.get('data').get('list').get('vlist')[num].get('pic')
        lastSlashIndex = coverUrl.rindex('/')
        imgName = coverUrl[lastSlashIndex + 1:]

        print("封面url : " + coverUrl)
        print("文件名 : " + imgName)

        urllib_download(folder, imgName, coverUrl)

else:
    print('该AV号不存在')
