"""
Class containing functions specific to the Wishlist page.

"""


from Amazon.page.basePage import BasePage
from Amazon.locators import locators
from selenium.webdriver.support import expected_conditions as ec


class WishlistPage(BasePage):
    def __init__(self, driver):
        """
        constructor
        """

        super().__init__(driver)

    def get_product_name(self):
        """
        It is used to get the name information of the product on the wishlist page.
        """

        product_name = self.find_element(*locators.WishListPageLocators.PRODUCT_NAME).text

        return product_name

    def delete_product_from_wishlist(self):
        """
        It is used to delete products from the wishlist.
        """

        self.click_element(locators.WishListPageLocators.DELETE_BUTTON)

    def delete_product_button_is_displayed(self):
        """
        It checks the information on the screen indicating that the product has been deleted from the Wishlist.
        """

        return self.displayed(locators.WishListPageLocators.DELETE_SUCCESS_INFORMATION)



