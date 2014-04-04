#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 03
"""

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# browser.get('http://www.baidu.com')
# assert u'百度一下' in browser.title
#
# elem = browser.find_element_by_name('wd')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
# browser.quit()



browser.get('http://www.bing.com')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.save_screenshot("screenshot.png")

