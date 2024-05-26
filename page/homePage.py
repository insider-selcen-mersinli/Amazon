from Amazon.page.basePage import BasePage
from Amazon.locators import locators
from selenium.webdriver.support import expected_conditions as ec


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def homepage_banner_is_displayed(self):
        return self.displayed(locators.HomePageLocators.HOME_PAGE_BANNER)

    def click_signin_page(self):
        self.click_element(locators.HomePageLocators.SIGN_IN_PAGE_BUTTON)

    def search_product(self, search_text):
        self.search_for(search_text)





