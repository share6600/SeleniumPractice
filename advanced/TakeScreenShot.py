from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Screenshots():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        destinationFileName = "C:\\Users\\Lulu HIDD\\Desktop\\seleniumScreenShot\\test.png"
        try:
            driver.save_screenshot(destinationFileName)
            print("screenshot saved on " + destinationFileName)

        except NotADirectoryError:
            print("not a directory issue")

ff = Screenshots()
ff.test()