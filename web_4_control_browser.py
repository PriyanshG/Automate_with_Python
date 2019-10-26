from selenium import webdriver

browser=webdriver.Firefox(executable_path='/run/media/priyansh/697BADB67547A75B/automate_the_things/geckodriver')
#browser=webdriver.Firefox()
add='https://automatetheboringstuff.com/'
browser.get(add)
sel='.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(1) > a:nth-child(1)'
elem=browser.find_element_by_css_selector(sel)
elem.click()
