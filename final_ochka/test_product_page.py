from BasePage.main_page import MainPage
from BasePage.product_page import ProductPage
from BasePage.locators import ShopPageLocators
import time
import pytest

bLink = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, bLink)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    basket_link = browser.find_element(*ShopPageLocators.ADD_TO_CART_BUTTON)
    basket_link.click()
    page.solve_quiz_and_get_code()
    page.buy_the_book()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    basket_link = browser.find_element(*ShopPageLocators.ADD_TO_CART_BUTTON) # add to basket
    basket_link.click()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.compare_product_names()
    page.buy_the_book()