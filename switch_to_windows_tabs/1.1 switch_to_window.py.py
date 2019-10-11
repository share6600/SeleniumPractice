from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandel = driver.current_window_handle
        print("current handel is "+parentHandel)
        time.sleep(2)
        # Find open window button and click it
        driver.find_element_by_id("openwindow").click()
        time.sleep(2)
        # Find all handles, there should two handles after clicking open window button
        handels = driver.window_handles
        # Switch to window and search course
        for handle in handels:
            print(handle)
        # Switch back and to parent handle


       # serch = driver.find_element_by_id("search-courses").send_keys("yyyy")

ff = SwitchToWindow()
ff.test()