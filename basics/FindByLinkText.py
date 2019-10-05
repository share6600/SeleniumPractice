from selenium import webdriver

class FindByLinkText():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        #driver = webdriver.Firefox(executable_path="/home/sharif/Downloads/geckodriver")
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByLinkText = driver.find_element_by_link_text("Login")
        if elementByLinkText is not None:
            print("WE FOUND THE ELEMENT by link text")
        elementByPartialLinkText = driver.find_element_by_partial_link_text("Prac")
        if elementByPartialLinkText is not None:
            print("WE FOUND THE ELEMENT by partial text")
ff = FindByLinkText()

ff.test()    