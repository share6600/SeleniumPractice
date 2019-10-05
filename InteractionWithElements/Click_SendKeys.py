from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Click_SendKeys():
    def testMethod(self):
        #driver = webdriver.Firefox(executable_path="/home/sharif/Downloads/geckodriver")
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//a[@class='navbar-link fedora-navbar-link']").click()
        emailInput = driver.find_element_by_id("user_email")
        time.sleep(1)
        emailInput.send_keys("aa@hotmail.com")
        passwordElement = driver.find_element(By.ID,"user_password")
        time.sleep(1)
        passwordElement.send_keys("12345")
        emailInput.clear()
        passwordElement.clear()
        time.sleep(1)
        emailInput.send_keys("bb@hotmail.com")
        time.sleep(1)
        passwordElement.send_keys("198775")
ff = Click_SendKeys()
ff.testMethod()   