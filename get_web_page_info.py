from selenium import webdriver
import time

url = 'https://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)

# 使用JavaScript开启新的窗口
js = 'window.open("https://www.baidu.com");'
driver.execute_script(js)

# 获取当前页面的窗口信息
current_window = driver.current_window_handle

# 获取浏览器的全部窗口信息
handles = driver.window_handles

# 设置延时查看效果
time.sleep(3)

# 根据窗口信息进行窗口切换
driver.switch_to.window(handles[0])
time.sleep(3)
driver.switch_to.window(handles[1])
