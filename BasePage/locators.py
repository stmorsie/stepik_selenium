from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'login')]")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FROM = (By.CSS_SELECTOR, "#register_form")