
from selenium.webdriver.common.by import By

from ProjectEbaySearch.page.advance_page import advance_page
from ProjectEbaySearch.page.product_page import product_page
from ProjectEbaySearch.page.welcome_page import welcome_page
from ProjectEbaySearch.test.seleniumBaseProjectEbaySearch import seleniumBaseProjectEbaySearch


# description test - The code is designed for searching any product on eBay.
# It opens the site, performs a search, sets advanced filters like price and location,
# displays relevant results, clicks on the first result,
# and proceeds to the checkout page.
# Automation for searching and purchasing products.

class research_product_test():
    base = seleniumBaseProjectEbaySearch()
    driver = base.selenium_init("https://www.ebay.com/")
    welcome_page_object = welcome_page(driver)
    product_page_object = product_page(driver)
    advance_page_object = advance_page(driver)

    welcome_page_object.research_bar_in_ebay("desktop")

    welcome_page_object.advance_button_for_item()

    advance_page_object.select_your_preference("hp", "500", "1500")

    advance_page_object.select_your_preference_add("United States", "Price + Shipping: lowest first")

    all_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "desktop")

    for desktop in all_links:
        print(desktop.text)

    product_page_object.click_to_first_link()

    product_page_object.go_to_checkout()

    base.selenium_end(driver)