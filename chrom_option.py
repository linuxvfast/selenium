from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.baidu.com'
# options类实例化
chrome_options = Options()
# 浏览器参数设置
# --headless是不显示浏览器启动及执行过程
chrome_options.add_argument('--headless')
# 设置浏览器的字符集
chrome_options.add_argument('lang=zh_CN.UTF-8')
# 设置反爬虫检查
UserAgent = '''Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 
            Chrome/79.0.3945.117 Safari/537.36'''
chrome_options.add_argument('User-Agent=' + UserAgent)
# 使用参数打开浏览器
driver = webdriver.Chrome(chrome_options=chrome_options)
# 浏览器最大化
driver.maximize_window()
# 浏览器最小化
driver.minimize_window()

driver.get(url)
# 获取网页标题
print(driver.title)
# 获取网页HTML代码
print(driver.page_source)
