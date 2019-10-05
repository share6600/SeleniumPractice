from selenium import webdriver

class FindByXpath_css():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        #driver = webdriver.Firefox(executable_path="/home/sharif/Downloads/geckodriver")
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")
        if elementByXpath is not None:
            print("WE FOUND THE ELEMENT by Xpath")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")
        if elementByCss is not None:
            print("WE FOUND THE ELEMENT by css ")
ff = FindByXpath_css()

ff.test()    