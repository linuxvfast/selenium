from selenium import webdriver

# 指定文件下载的保存位置
options = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome()
driver.get('https://pc.weixin.qq.com')
driver.maximize_window()
driver.find_element_by_class_name('button').click()
