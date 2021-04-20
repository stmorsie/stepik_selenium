from BasePage.base_page import BasePage
from BasePage.product_page import ProductPage
from BasePage.locators import ShopPageLocators
from BasePage.basket_page import BasketPage
from BasePage.login_page import LoginPage

import time
import pytest

bLink = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


#pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.compare_product_names()
    page.buy_the_book()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.open_basket()
    basket_page.is_basket_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_card()
    item_page.is_not_element_present()


@pytest.mark.xfail(strict=True)
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_card()
    item_page.is_not_element_present(*ShopPageLocators.MESSAGE_ADD)


@pytest.mark.login_auth
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.browser = browser
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page_login = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        page_login.open()
        page_login.register_new_user(email, password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        item_page = ProductPage(self.browser, self.link)
        item_page.open()
        item_page.add_to_card()
        item_page.check_product_name_on_page_and_in_message()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.is_not_element_present()  # *ShopPageLocators.MESSAGE_ADD
