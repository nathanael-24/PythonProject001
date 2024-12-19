from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# description page - This page is intended for selecting filters within the advance page.

class advance_page():
    def __init__(self,driver):
        self.driver = driver
        self.exclude_words_locator = "_ex_kw"
        self.title_and_description_locator = "s0-1-17-5[1]-[0]-LH_TitleDesc"
        self.show_items_priced_min_locator = "s0-1-17-5[2]-@range-comp[]-@range-textbox[]-textbox"
        self.show_items_priced_max_locator = "s0-1-17-5[2]-@range-comp[]-@range-textbox[]_1-textbox"
        self.buy_it_now_locator = "s0-1-17-6[3]-[2]-LH_BIN"
        self.not_specified_condition_locator = "s0-1-17-6[4]-[2]-LH_ItemCondition"
        self.to_destination_drop_down_locator = "s0-1-17-6[7]-5[@field[]]_1-_saact"
        self.show_low_prices_first_locator = "s0-1-17-8[9]-1[0]-_sop"
        self.submit_button_locator = "button[type='submit']"

    def select_your_preference (self, enter_exclude_word, min_price, max_price):
        exclude_words = self.driver.find_element(By.ID, self.exclude_words_locator)
        assert exclude_words is not None, "Error: Exclude_words not found"
        title_and_description = self.driver.find_element(By.ID, self.title_and_description_locator)
        assert title_and_description is not None, "Error: Title_and_description not found"
        show_items_priced_min = self.driver.find_element(By.ID, self.show_items_priced_min_locator)
        assert show_items_priced_min is not None, "Error: Show_items_priced_min not found"
        show_items_priced_max = self.driver.find_element(By.ID, self.show_items_priced_max_locator)
        assert show_items_priced_max is not None, "Error: Show_items_priced_max not found"
        buy_it_now = self.driver.find_element(By.ID, self.buy_it_now_locator)
        assert buy_it_now is not None, "Error: Buy_it_now not found"
        not_specified_condition = self.driver.find_element(By.ID, self.not_specified_condition_locator)
        assert not_specified_condition is not None, "Error: Not_specified_condition not found "

        exclude_words.click()
        exclude_words.send_keys(enter_exclude_word)

        title_and_description.click()

        show_items_priced_min.click()
        show_items_priced_min.send_keys(min_price)
        show_items_priced_max.click()
        show_items_priced_max.send_keys(max_price)

        buy_it_now.click()

        not_specified_condition.click()
        print("select your preference is working")

    def select_your_preference_add (self ,destination ,low_prices_first):
        to_destination_drop_down = self.driver.find_element(By.ID ,self.to_destination_drop_down_locator)
        show_low_prices_first = self.driver.find_element(By.ID ,self.show_low_prices_first_locator)
        submit_button =  self.driver.find_element(By.CSS_SELECTOR ,self.submit_button_locator)

        select_to_destination_drop_down = Select(to_destination_drop_down)
        select_to_destination_drop_down.select_by_visible_text(destination)

        select_show_low_prices_first = Select(show_low_prices_first)
        select_show_low_prices_first.select_by_visible_text(low_prices_first)

        submit_button.click()