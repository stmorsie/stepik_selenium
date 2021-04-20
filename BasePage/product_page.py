from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ShopPageLocators


class ProductPage(BasePage):
    def buy_the_book(self):
        template = "Your basket total is now {}"
        book_price = self.browser.find_element(*ShopPageLocators.BOOK_PRICE).text
        cart_size = self.browser.find_element(*ShopPageLocators.BASKET_PRICE).text
        assert template.format(book_price) == template.format(cart_size), 'цена {} не равна {}'.format(book_price, cart_size)

    def compare_product_names(self):
        template = "{} has been added to your basket."
        message = self.browser.find_element(*ShopPageLocators.MESSAGE_ADD).text
        book_name = self.browser.find_element(*ShopPageLocators.BOOK_NAME).text
        assert template.format(message) == template.format(book_name), 'нет названия книги {message}'.format(message=message)
    def get_product_name(self)->str:
        try:
            return self.browser.find_element(*ShopPageLocators.BOOK_NAME).text
        except NoSuchElementException:
            return None

    def get_success_message_after_add_product_to_basket(self) -> str:
        WebDriverWait(self.browser, 20).until(
            expected_conditions.presence_of_element_located(ShopPageLocators.MESSAGE_ADD))
        try:
            return self.browser.find_element(*ShopPageLocators.MESSAGE_ADD).text
        except NoSuchElementException:
            return None
    def check_product_name_on_page_and_in_message(self):
        result = self.get_success_message_after_add_product_to_basket()
        product_name = self.get_product_name()

        assert result == product_name, 'Product name dont equal'
    def add_to_card(self)->bool:
        try:
            self.browser.find_element(*ShopPageLocators.ADD_TO_CART_BUTTON).click()
            return True
        except NoSuchElementException:
            return False