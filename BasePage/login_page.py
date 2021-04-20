from BasePage.base_page import BasePage
from BasePage.locators import LoginPageLocators
import time

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "There is not 'login' in the link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "There is no registration form"

    def register_new_user(self, email, password, times=20):
        self.browser.get('http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        self.browser.find_element(*LoginPageLocators.REGISTER_LOGIN_TEXTBOX).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSPORT_TEXTBOX).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSPORT_TEXTBOX).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()



