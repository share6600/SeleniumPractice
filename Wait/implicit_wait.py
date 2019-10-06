from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class implicit_wait():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginlink =  driver.find_element_by_xpath("//a[@class='navbar-link fedora-navbar-link']")
        loginlink.click()

        loginemail = driver.find_element_by_xpath("//input[@id='user_email']")
        loginemail.send_keys("aa@g.com")
        loginpass = driver.find_element_by_xpath("//input[@id='user_password']")
        time.sleep(2)
        loginpass.send_keys("1223324")

ff = implicit_wait()
ff.test()