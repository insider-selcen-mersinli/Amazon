from Amazon.locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)

    def click_element(self, by_locator):
        self.wait.until(ec.presence_of_element_located(by_locator)).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def send_text(self, text, *by_locator):
        self.find_element(*by_locator).send_keys(text)

    def search_for(self, search_string):
        self.wait.until(ec.presence_of_element_located(locators.HomePageLocators.SEARCH_BAR))
        self.send_text(search_string, *locators.HomePageLocators.SEARCH_BAR)
        self.click_element(locators.HomePageLocators.SEARCH_SUBMIT_BUTTON)

    def displayed(self, by_locator):
        return self.wait.until(ec.presence_of_element_located(by_locator)).is_displayed()
