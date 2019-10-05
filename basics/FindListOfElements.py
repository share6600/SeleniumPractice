
from selenium import webdriver
from selenium.webdriver.common.by import By
class FindListOfElements():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        #driver = webdriver.Firefox(executable_path="/home/sharif/Downloads/geckodriver")
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementsById = driver.find_elements_by_id("name")
        length = len(elementsById)
        if elementsById is not None:
            print("WE FOUND THE ELEMENTs and length of them is "+ str(length))
        elementsByTag = driver.find_elements(By.TAG_NAME,"div")
        length2 = len(elementsByTag)
        if elementsByTag is not None:
            print("WE FOUND THE ELEMENTs by tag and length of them is "+ str(length2))
ff = FindListOfElements()

ff.test()    