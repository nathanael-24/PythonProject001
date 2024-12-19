from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class seleniumBaseProjectEbaySearch():

    #base = seleniumBaseProjectEbaySearch()  driver = base.selenium_init("")
    def selenium_init(self,url):
        print ("test start")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        return driver



        # base.selenium_end(driver)
    def selenium_end(self,driver):
        driver.close()
        print ("test end")




