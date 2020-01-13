import requests

url = 'https://www.baidu.com'
res = requests.get(url)

# 获取RequestsCookieJar对象
print(res.cookies)
mycookies = res.cookies
# RequestsCookieJar对象转换字典
cookie_dict = requests.utils.dict_from_cookiejar(mycookies)
print(cookie_dict)

#cookie以字典形式写入文件
#写入文件
with open('cookies.txt','w',encoding='utf-8') as f:
    f.write(str(cookie_dict))

#读取文件
with open('cookies.txt','r') as f:
    dict_value = f.read()
    print(eval(dict_value)) #转换字符串为字典
    r = requests.get(url,cookies=eval(dict_value))
    print(r.status_code)

# 字典转RequestsCookieJar对象
cookie_jar = requests.utils.cookiejar_from_dict(cookie_dict, overwrite=True)
print(cookie_jar)
# 把RequestsCookieJar对象添加cookies字典中
print(requests.utils.add_dict_to_cookiejar(mycookies, cookie_dict))

