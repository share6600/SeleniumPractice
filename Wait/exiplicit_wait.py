from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import ast
class ExplicitWaitDemo1():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/24/2019")
        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnDate.clear()
        returnDate.send_keys("12/26/2019")
        driver.find_element(By.XPATH, "//button[@class='btn-primary btn-action gcw-submit']").click()
        time.sleep(1)
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        elbutton = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                         "//ul[@id='flightModuleList']//li//span[contains(text(), '$')]")))
        felement = wait.until(EC.presence_of_element_located((By.XPATH,
                                                         "//ul[@id='flightModuleList']//li[1]//span[contains(text(), '$')]")))

        all_prices = [] 
        for elb in elbutton: 
          all_prices.append(elb.text[1:])


        print(str(felement.text))
        all_prices.sort()
        m = min(all_prices)
        print(str())

       # for item in all_prices:
       #   print(str(item))
                                                              
       #   element.click()
       # print(str(len(element)))
        time.sleep(2)


ff = ExplicitWaitDemo1()
ff.test()