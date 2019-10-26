
from selenium import webdriver
browser=webdriver.Chrome(executable_path='chromedriver')
add='https://a2oj.com/'
browser.get(add)
sel='Username'
sear=browser.find_elements_by_id('Username')
print(sear)
sear.send_keys('C++')
sear.submit()
print(browser)

