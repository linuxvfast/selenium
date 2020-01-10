from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

url = 'https://www.baidu.com'

# path = 'H:\Python36\chromedriver.exe'
browser = webdriver.Chrome()
browser.get(url)

# 输入框输入内容
element = browser.find_element_by_id('kw')
element.send_keys('java 你')
time.sleep(2)

# 删除最后的文字
element.send_keys(Keys.BACK_SPACE)
time.sleep(2)

# 添加空格+教程
element.send_keys(Keys.SPACE)
element.send_keys("教程")
time.sleep(2)

# ctrl+a快捷键
element.send_keys(Keys.CONTROL, 'a')
time.sleep(2)
# ctrl+x快捷键
element.send_keys(Keys.CONTROL, 'x')
time.sleep(2)
# ctrl+v快捷键
element.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 回车代替鼠标单击
browser.find_element_by_id('su').send_keys(Keys.ENTER)
