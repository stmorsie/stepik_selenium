from BasePage.main_page import MainPage
from BasePage.product_page import ProductPage
from BasePage.locators import ShopPageLocators
import time

bLink = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, bLink)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    basket_link = browser.find_element(*ShopPageLocators.BAG_BUTTON)
    basket_link.click()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.buy_the_book()  # выполняем метод стрницы — переходим на страницу логина