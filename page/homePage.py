"""
Class containing functions specific to the Home page.
"""


from Amazon.page.basePage import BasePage
from Amazon.locators import locators
from selenium.webdriver.support import expected_conditions as ec


class HomePage(BasePage):
    def __init__(self, driver):
        """
        constructor

        """

        super().__init__(driver)

    def homepage_banner_is_displayed(self):
        """
        Homepage checks whether the banner is displayed or not. Thus, we understand whether we are on the homepage or not.

        """

        return self.displayed(locators.HomePageLocators.HOME_PAGE_BANNER)

    def click_signin_page(self):
        """
        Switches to the sign_in page
        """        

        self.click_element(locators.HomePageLocators.SIGN_IN_PAGE_BUTTON)

    def search_product(self, search_text):
        """
        Searches for products via search bar
        """

        self.search_for(search_text)





