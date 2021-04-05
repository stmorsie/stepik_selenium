from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'login')]")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FROM = (By.CSS_SELECTOR, "#register_form")


class ShopPageLocators():
    BAG_BUTTON = (By.XPATH, "//button[contains(text(),'Add to basket')]")
    PRICE_FINAL = (By.CSS_SELECTOR, "div>div>div>p>strong")
    PRICE_REAL = (By.CSS_SELECTOR, "p.price_color")
