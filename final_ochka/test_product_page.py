from BasePage.base_page import BasePage
from BasePage.product_page import ProductPage
from BasePage.locators import ShopPageLocators
from BasePage.basket_page import BasketPage
from BasePage.login_page import LoginPage

import time
import pytest

bLink = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket_bonus(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    basket_link = browser.find_element(*ShopPageLocators.ADD_TO_CART_BUTTON)
    basket_link.click()
    page.solve_quiz_and_get_code()
    page.compare_product_names()
    page.buy_the_book()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, bLink)
    page.open()
    basket_link = browser.find_element(*ShopPageLocators.ADD_TO_CART_BUTTON)
    basket_link.click()
    page.solve_quiz_and_get_code()
    page.buy_the_book()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.open_basket()
    basket_page.is_basket_empty()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_card()
    item_page.is_not_element_present()


def test_guest_cant_see_success_message(self, browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.is_not_element_present(*ShopPageLocators.MESSAGE_ADD)


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page_login = LoginPage(browser, link)
        page_login.open()
        page_login.register_new_user(email, password)
        page_base = BasePage(browser, link)
        page_base.should_be_authorized_user()
    def test_user_can_add_product_to_basket(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.add_to_card()
        item_page.check_product_name_on_page_and_in_message()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.is_not_element_present(*ShopPageLocators.MESSAGE_ADD)
