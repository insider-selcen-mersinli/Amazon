"""
Class containing functions specific to the Category page.

"""


from Amazon.page.basePage import BasePage
from Amazon.locators import locators
from selenium.webdriver.support import expected_conditions as ec


class CategoryPage(BasePage):
    def __init__(self, driver):
        """
        constructor
        """

        super().__init__(driver)

    def select_page(self):
        """
        When the amount of products is large on the Category page, the products are divided into pages. This function allows switching to the desired page.
        """

        self.click_element(locators.CategoryPageLocators.PAGE_NUMBER_AREA)

    def select_product(self):
        """
        It allows you to select the desired product and go into the product.
        """

        self.click_element(locators.CategoryPageLocators.PRODUCT_IMAGE)

    def get_search_keyword(self):
        """
        The search bar also retrieves the word whose results are shown to check that the results of the word you searched are correct.
        """

        search_text = self.find_element(*locators.CategoryPageLocators.SEARCH_RESULT_CONTROL).text.strip('"')
        return search_text

    def get_page_number(self):
        """
        It retrieves the page number to check whether the desired page is navigated or not.
        """
        
        return self.wait.until(ec.presence_of_element_located(locators.CategoryPageLocators.PAGE_NUMBER)).text.strip()
