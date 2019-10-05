from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Click_SendKeys():
    def testMethod(self):
        #driver = webdriver.Firefox(executable_path="/home/sharif/Downloads/geckodriver")
        driver = webdriver.Firefox()
        baseUrl = "https://www.google.com/"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        targetElement = driver.find_element_by_xpath("//input[@name='q']")
        e1State = targetElement.is_enabled()
        if e1State is True:
          targetElement.send_keys("where is bahrain")

ff = Click_SendKeys()
ff.testMethod()  