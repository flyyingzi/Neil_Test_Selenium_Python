#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 30
"""

# 1 测试计算器
from appium import webdriver
import os
import time
import desired_capabilities


# desired_caps = dict()
# desired_caps['device'] = 'android'
# desired_caps['browserName'] = ''
# desired_caps['version'] = '4.4'
# desired_caps['app-package'] = 'com.android.calculator2'
# desired_caps['app-activity'] = '.Calculator'

desired_caps = desired_capabilities.get_desired_capabilities()


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 点击计算器上的数字和运算符

driver.find_element_by_name('1').click()
time.sleep(1)
driver.find_element_by_name(u'删除').click()
time.sleep(1)
driver.find_element_by_name('2').click()
time.sleep(1)
driver.find_element_by_name('+').click()
time.sleep(1)
driver.find_element_by_name('1').click()
time.sleep(1)
driver.find_element_by_name('=').click()
time.sleep(1)
driver.quit()




