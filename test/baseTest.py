"""
Base class containing setUp and tearDown functions common to each test.

"""


import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Amazon.page.basePage import BasePage
from Amazon.page.categoryPage import CategoryPage
from Amazon.page.homePage import HomePage
from Amazon.page.loginPage import LoginPage
from Amazon.page.productPage import ProductPage
from Amazon.page.wishlistPage import WishlistPage


class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        Basic preparations before the test starts

        """

        """
        chrome_options = webdriver.ChromeOptions()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

        self.driver.get("https://www.amazon.com/")

        self.base = BasePage(self.driver)
        self.home = HomePage(self.driver)
        self.login = LoginPage(self.base)
        self.category = CategoryPage(self.base)
        self.product = ProductPage(self.base)
        self.wishlist = WishlistPage(self.base)

    def tearDown(self):
        """
        Closing procedures at the end of the test
        
        """

        self.driver.quit()
