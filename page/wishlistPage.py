from Amazon.page.basePage import BasePage
from Amazon.locators import locators
from selenium.webdriver.support import expected_conditions as ec


class WishlistPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_name(self):
        product_name = self.find_element(*locators.WishListPageLocators.PRODUCT_NAME).text

        return product_name

    def delete_product_from_wishlist(self):
        self.click_element(locators.WishListPageLocators.DELETE_BUTTON)

    def delete_product_button_is_displayed(self):
        return self.displayed(locators.WishListPageLocators.DELETE_SUCCESS_INFORMATION)



