from selenium.webdriver.common.by import By


class HomePageLocators:
    HOME_PAGE_BANNER = (By.ID, 'pageContent')
    SIGN_IN_PAGE_BUTTON = (By.ID, "nav-link-accountList")
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON = (By.ID, "nav-search-submit-button")


class LoginPageLocators:
    EMAIL_AREA = (By.ID, "ap_email")
    CONTINUE_BUTTON = (By.ID, "continue")
    PASSWORD_AREA = (By.NAME, "password")
    SIGNIN_BUTTON = (By.ID, "signInSubmit")


class CategoryPageLocators:
    SEARCH_RESULT_CONTROL = (By.CSS_SELECTOR, ".a-color-state")
    PAGE_NUMBER_AREA = (By.CSS_SELECTOR, "a[aria-label = 'Go to page 2']")
    PRODUCT_IMAGE = (By.XPATH, "//div[@data-index='4']//h2/a")
    PAGE_NUMBER = (By.CSS_SELECTOR, '.s-pagination-selected')


class ProductPageLocators:
    PRODUCT_NAME = (By.ID, 'productTitle')
    ADD_TO_LIST_BUTTON = (By.ID, "wishListDropDown")
    ADD_TO_WISHLIST = (By.ID, "atwl-list-name-1PNKC34WSXPSF")
    WISHLIST_PAGE_LINKER = (By.ID, "huc-list-link")


class WishListPageLocators:
    PRODUCT_NAME = (By.XPATH, '//h2/a[@class="a-link-normal"]')
    DELETE_BUTTON = (By.NAME, "submit.deleteItem")
    DELETE_SUCCESS_INFORMATION = (By.CLASS_NAME, 'a-alert-inline-success')
