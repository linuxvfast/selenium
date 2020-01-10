from selenium import webdriver

url = 'https://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)

# 隐性等待，最长等待时间为30秒
# driver.implicitly_wait(10)
# driver.find_element_by_id('kw').send_keys('python')

# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# visibility_of_element_located  检查网页元素是否可见
# (By.ID,'kw)    kw是搜索框的id属性值,By.ID是使用find_element_by_id定位
condition = expected_conditions.visibility_of_element_located((By.ID, 'kw'))
WebDriverWait(driver=driver, timeout=5, poll_frequency=0.5).until(condition)

'''
隐性等待是指在一个设定的时间内检测网页是否加载完成，也就是一般情况下你看到浏览器标签栏那个小圈不再转，
才会执行下一步。比如代码中设置30秒等待时间，网页只要在30秒内完成加载就会自动执行下一步，
如果超出30秒就会抛出异常。值得注意的是，隐性等待对整个driver的周期都起作用，所以只要设置一次即可。

显性等待能够根据判断条件而进行灵活地等待，程序每隔一段时间检测一次，如果检测结果与条件成立了，则执行下一步，
否则继续等待，直到超过设置的最长时间为止，然后抛出TimeoutException异常。显性等待的使用涉及到多个模块，包括By、
expected_conditions和WebDriverWait，各个模块说明如下。

By：设置元素定位方式，定位方式共8种：ID、XPATH、LINK_TEXT、PARTIAL_LINK_TEXT、NAME、
                                        TAG_NAME、CLASS_NAME、CSS_SELECTOR。
expected_conditions：验证网页元素是否存在，提供了多种验证方式。具体可以查看源码：
    Lib\site-packages\selenium\webdriver\support\expected_conditions.py

WebDriverWait的参数说明如下。
    driver：浏览器对象driver。
    timeout：超时时间，等待的最长时间。
    poll_frequency：检测时间的间隔。
    ignored_exceptions：忽略的异常，如果在调用until或until_not的过程中抛出的异常在这个参数里，则不中断代码，
    继续等待，如果抛出的异常在这个参数之外，则中断代码并抛出异常。默认值为NoSuchElementException。
    until：条件判断，参数必须为expected_conditions对象。如果网页里某个元素与条件符合，则中断等待并执行下一个步骤。
    until_not：与until的逻辑相反。
    
隐性等待和显性等待相比于time.sleep这种强制等待更为灵活和智能，可解决各种网络延误的问题，
    隐性等待和显性等待可以同时使用，但最长的等待时间取决于两者之间的最大数，如上述代码的隐性等待时间为30，
    显性等待时间为20，则该代码的最长等待时间为隐性等待时间。
'''
