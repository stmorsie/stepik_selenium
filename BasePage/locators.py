from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'login')]")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FROM = (By.CSS_SELECTOR, "#register_form")


class ShopPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD = (By.CSS_SELECTOR, ".alertinner > strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
