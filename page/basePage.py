"""
The base class that contains common functions to be used for each page, that is, for each class.

"""


from Amazon.locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        """
        Constructor
        """

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)

    def click_element(self, by_locator):
        """
        Click function
        Performs a click operation on the selected element.
        """

        self.wait.until(ec.presence_of_element_located(by_locator)).click()

    def find_element(self, *locator):
        """
        This function allows finding the element whose locator information is given.
        """

        return self.driver.find_element(*locator)

    def send_text(self, text, *by_locator):
        """
        It is used to send login information to elements that can receive input.
        """

        self.find_element(*by_locator).send_keys(text)

    def search_for(self, search_string):
        """
        Search bar is a common and constant area for the website. The search process is the same on every page. This function allows us to search via the search bar.
        """

        self.wait.until(ec.presence_of_element_located(locators.HomePageLocators.SEARCH_BAR))
        self.send_text(search_string, *locators.HomePageLocators.SEARCH_BAR)
        self.click_element(locators.HomePageLocators.SEARCH_SUBMIT_BUTTON)

    def displayed(self, by_locator):
        """
        This function controls the display of the element whose locator information is given.
        """

        return self.wait.until(ec.presence_of_element_located(by_locator)).is_displayed()
