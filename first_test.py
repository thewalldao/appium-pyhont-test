# Android environment
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


desired_caps = dict(
    platformName='Android',
    platformVersion='10',
    automationName='uiautomator2',
    deviceName='PDAGAA48A1307990',
    appPackage='com.bal.approvaltime',
    appActivity='com.bal.approvaltime.MainActivity',
    noReset=True,
)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
actions = TouchAction(driver)


elskip = driver.find_element_by_xpath("//android.widget.FrameLayout[@resource-id='android:id/content']//android.widget.TextView[@text='Skip This Step']")
elhamburger_button =driver.find_element_by_xpath("(//android.widget.FrameLayout[@resource-id='android:id/content']//android.widget.TextView)[1]/..")
actions.tap(elskip).perform()
time.sleep(0.5)
# elhamburger_button.click()
actions.tap(elhamburger_button).perform()

