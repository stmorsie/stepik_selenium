from BasePage.main_page import MainPage
from BasePage.base_page import BasePage
from BasePage.product_page import ProductPage
from BasePage.locators import ShopPageLocators
import time
import pytest

bLink = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser,
                       bLink)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    basket_link = browser.find_element(*ShopPageLocators.ADD_TO_CART_BUTTON)
    basket_link.click()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.buy_the_book()


@pytest.mark.parametrize('link', BasePage.offer_link(8))
def test_guest_can_add_product_to_basket_bonus(browser, link):
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    basket_link = browser.find_element(*ShopPageLocators.ADD_TO_CART_BUTTON)  # add to basket
    basket_link.click()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.compare_product_names()
    page.buy_the_book()
