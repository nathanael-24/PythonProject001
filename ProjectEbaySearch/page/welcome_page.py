from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# description page - This page is intended for searching a product and opening the Advance window.

class welcome_page():
    def __init__(self,driver):
        self.driver = driver
        self.research_bar_locator = "gh-ac"
        self.advance_button_locator = "gh-as-a"

    def research_bar_in_ebay (self,research_text):
        print("The research bar is being tested...")
        research = self.driver.find_element(By.ID, self.research_bar_locator)
        assert research is not None, "Error: Research bar not found!"
        print("Success: Research bar found")
        research.click()
        research.send_keys(research_text)
        research.send_keys(Keys.ENTER)
        print("The research bar is working as expected.")

    def advance_button_for_item (self):
        advance = self.driver.find_element(By.ID, self.advance_button_locator)
        assert advance is not None, "Error: Advance button not found!"
        print("Success: Advance button found")
        advance.click()
        print("advance button working")


      
















