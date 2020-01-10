from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.youdao.com')
time.sleep(5)

# 添加cookies
driver.add_cookie({'name': 'Login_User', 'value': 'PassWord'})

# 获取全部cookies
all_cookies = driver.get_cookies()
print('all cookies:', all_cookies)

# 获取name为Login_User的cookie内容
name_cookie = driver.get_cookie('Login_User')
print('name_cookie:', name_cookie)

# 删除name为Login_User的cookie
driver.delete_cookie('Login_User')
surplus_cookies = driver.get_cookies()
print('剩余cookie:', surplus_cookies)

# 删除全部cookie
driver.delete_all_cookies()
surplus_cookies = driver.get_cookies()
print('剩余cookie:', surplus_cookies)
