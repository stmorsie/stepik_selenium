from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'login')]")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_USERNAME_TEXTBOX = (By.ID, 'id_login-username')
    LOGIN_PASSWORD_TEXTBOX = (By.ID, 'id_login-password')
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="login_submit"]')

    REGISTER_LOGIN_TEXTBOX = (By.ID, 'id_registration-email')
    REGISTER_PASSPORT_TEXTBOX = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASSPORT_TEXTBOX = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="registration_submit"]')

    SUCCESS_REGISTER = (By.CSS_SELECTOR, 'div#messages>div>div>i.icon-ok-sign')


class ShopPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD = (By.CSS_SELECTOR, ".alertinner>strong:nth-child(1)")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini>span>a')

    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class OtzivPage():
    PRESS_YES = (By.CSS_SELECTOR, "#mess705241>div.ozenka-otzyva>span>a")
