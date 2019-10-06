from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DrpDownList():

    def testListOfElements(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        element = driver.find_element_by_id("carselect")
        elm = Select(element)
        ELMBYVALUE = elm.select_by_value("benz")
        print("select Benz by value")
        time.sleep(2)
        
        ELMBYINDEX = elm.select_by_index("2")
        print("select Honda by index")
        time.sleep(2)
        
        ELMBYITEXT = elm.select_by_visible_text("BMW")
        print("select bmw by Visible text")
        time.sleep(2)
        
        ELMBYINDEX = elm.select_by_index("2")
        print("select Honda by index")


ff = DrpDownList()
ff.testListOfElements()