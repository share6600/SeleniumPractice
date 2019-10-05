from selenium import webdriver

class FindByClass_Tag():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        #driver = webdriver.Firefox(executable_path="/home/sharif/Downloads/geckodriver")
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByClassName = driver.find_element_by_class_name("inputs")
        elementByClassName.send_keys("im input")
        if elementByClassName is not None:
            print("WE FOUND THE ELEMENT by class")

        elementByTagName = driver.find_element_by_tag_name("footer")
        if elementByTagName is not None:
            print("WE FOUND THE ELEMENT by tag")

        elementByTagName2 = driver.find_element_by_tag_name("h1")

        text = elementByTagName2.text   
        print("WE FOUND THE ELEMENT by tag2 and the text inside it is :" + text)             
ff = FindByClass_Tag()

ff.test()    