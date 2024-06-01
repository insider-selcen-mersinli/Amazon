"""
Class containing functions specific to the Product page.

"""


from Amazon.page.basePage import BasePage
from Amazon.locators import locators


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_name(self):
        """
        Gets the name of the product for some checks to be made
        """

        product_name = self.find_element(*locators.ProductPageLocators.PRODUCT_NAME).text

        return product_name

    def add_to_wishlist(self):
        """
        Adds the product to the wishlist
        """
        
        self.click_element(locators.ProductPageLocators.ADD_TO_LIST_BUTTON)
        self.click_element(locators.ProductPageLocators.ADD_TO_WISHLIST)
        self.click_element(locators.ProductPageLocators.WISHLIST_PAGE_LINKER)
