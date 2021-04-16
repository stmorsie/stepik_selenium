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