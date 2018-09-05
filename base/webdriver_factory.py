from selenium import webdriver
import os
from base.basepage import BasePage



class Browser_Factory(BasePage):

    baseURL = "https://www.surveymonkey.com/"
    browser = "Chrome"

    def __init__(self, browser):

        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def select_browser(self):
        browser = Browser_Factory.browser
        if browser == "Chrome":
            return Browser_Factory.chrome(self)
        elif browser == "Firefox":
            return Browser_Factory.firebox(self)
        elif browser == "IE":
            return Browser_Factory.ie(self)
        else:
            print("Please Select Proper Browser")
            return 0

    def chrome(self):
        driverLocation = "D:\\Automation\\chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get(Browser_Factory.baseURL)
        driver.maximize_window()
        return driver

    def firebox(self):
        driver = webdriver.Firefox()
        driver.get(Browser_Factory.baseURL)
        driver.maximize_window()
        return driver

    def ie(self):
        driverLocation = "D:\\Automation\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverLocation
        driver = webdriver.Ie(driverLocation)
        driver.get(Browser_Factory.baseURL)
        driver.maximize_window()
        return driver
