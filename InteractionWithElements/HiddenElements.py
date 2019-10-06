from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def testletpractice(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        SHOW_BUTTON = driver.find_element_by_id("show-textbox")
        HIDE_DISPLAYED_INPUT = driver.find_element_by_id("displayed-text")
        status_HIDE_DISPLAYED_INPUT = HIDE_DISPLAYED_INPUT.is_displayed()
        time.sleep(2)

        if not status_HIDE_DISPLAYED_INPUT:
            SHOW_BUTTON.click()
            time.sleep(2)
        HIDE_DISPLAYED_INPUT.send_keys("im input text")
            

      #  driver.quit()
    

ff = WorkingWithElementsList()
ff.testletpractice()
#ff.testListOfElements()