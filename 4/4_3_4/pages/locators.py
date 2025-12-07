from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .basket-mini")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")