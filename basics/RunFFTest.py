from selenium import webdriver

class RunFFTest():
    def testMethod(self):
        #driver = webdriver.Firefox(executable_path="/home/sharif/Downloads/geckodriver")
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")

ff = RunFFTest()
ff.testMethod()      
