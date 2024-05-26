from Amazon.page.basePage import BasePage
from Amazon.locators import locators
from selenium.webdriver.support import expected_conditions as ec


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_page(self):
        self.click_element(locators.CategoryPageLocators.PAGE_NUMBER_AREA)

    def select_product(self):
        self.click_element(locators.CategoryPageLocators.PRODUCT_IMAGE)

    def get_search_keyword(self):
        search_text = self.find_element(*locators.CategoryPageLocators.SEARCH_RESULT_CONTROL).text.strip('"')
        return search_text

    def get_page_number(self):
        return self.wait.until(ec.presence_of_element_located(locators.CategoryPageLocators.PAGE_NUMBER)).text.strip()
