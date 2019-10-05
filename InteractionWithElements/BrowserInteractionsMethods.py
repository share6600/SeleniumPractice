from selenium import webdriver

class BrowserInteractions():
    def testMethod(self):
        BaseUrl = "https://learn.letskodeit.com/p/practice"
        #driver = webdriver.Firefox(executable_path="/home/sharif/Downloads/geckodriver")
        driver = webdriver.Firefox()
        # Window Maximize
        driver.maximize_window()    
        # Open the Url
        driver.get(BaseUrl)      
        # Get Title
        title = driver.title
        print("the title of the site is "+ title)
        #Get Current Url
        currentUrl = driver.get(driver.current_url)
        print("the current page is "+str(currentUrl))
        #Browser Refresh
        driver.refresh()
        print("this is the first refresh")
        driver.get(driver.current_url)
        print("this is the second refresh")
        #Open Anpother Url
        driver.get("https://google.com")
        #bROWSER Back
        driver.back()
        print("i went one step back in browser history")
        #Browser Forward
        driver.forward()
        print("i went one step forward in browser history")
        #Get the Page Source
        pageSource = driver.page_source()
        #driver close , quit
        driver.quit()
        #driver.close()


ff = BrowserInteractions()
ff.testMethod()    