#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 03
"""

# http://www.cnblogs.com/fnng/p/3193955.html
# 定位一组元素

from selenium_test import webdriver
from selenium_test.webdriver.support.ui import WebDriverWait
import time
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('level_locate.html')
dr.get(file_path)

#点击Link1链接（弹出下拉列表）
dr.find_element_by_link_text('Link1').click()

#找到id 为dropdown1的父元素
WebDriverWait(dr, 10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())
#在父亲元件下找到link为Action的子元素
menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Action')

#鼠标定位到子元素上
webdriver.ActionChains(dr).move_to_element(menu).perform()

time.sleep(2)

dr.quit()


