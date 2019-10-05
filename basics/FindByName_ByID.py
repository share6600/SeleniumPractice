from selenium import webdriver

class FindByName():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        #driver = webdriver.Firefox(executable_path="/home/sharif/Downloads/geckodriver")
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")
        if elementById is not None:
            print("WE FOUND THE ELEMENT by ID")
        elementByName = driver.find_element_by_name("show-hide")
        if elementByName is not None:
            print("WE FOUND THE ELEMENT by name")
ff = FindByName()

ff.test()    