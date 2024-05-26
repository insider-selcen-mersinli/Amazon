import time

from Amazon.page.basePage import BasePage
from Amazon.locators import locators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.send_text(email, *locators.LoginPageLocators.EMAIL_AREA)
        self.click_element(locators.LoginPageLocators.CONTINUE_BUTTON)
        self.send_text(password, *locators.LoginPageLocators.PASSWORD_AREA)
        self.click_element(locators.LoginPageLocators.SIGNIN_BUTTON)
        time.sleep(40)

