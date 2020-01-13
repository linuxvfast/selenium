import requests

#下载文件
url = 'https://dldir1.qq.com/weixin/Windows/WeChatSetup.exe'
r = requests.get(url)
with open('WeChatSetup.exe','wb') as f:
    f.write(r.content)

