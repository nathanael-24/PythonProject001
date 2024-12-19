from selenium.webdriver.common.by import By

# description page - This page is intended for clicking the first link after
# filtering and navigating to the "Add to Cart" page.

class product_page():
    def __init__(self,driver):
        self.driver = driver
        self.first_link_button_locator = "div[class='s-item__title']"
        self.add_to_card_button_locator = "atcBtn_btn_1"

    def click_to_first_link(self):
        first_link_button = self.driver.find_elements(By.CSS_SELECTOR,self.first_link_button_locator)
        first_link_button[2].click()

    def go_to_checkout(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        add_to_card_button = self.driver.find_element(By.ID,self.add_to_card_button_locator)
        add_to_card_button.click()