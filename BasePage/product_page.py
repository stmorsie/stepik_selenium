from .base_page import BasePage
from .locators import ShopPageLocators


class ProductPage(BasePage):
    def buy_the_book(self):
        real_price = self.is_element_present(*ShopPageLocators.PRICE_REAL)
        basket_price = self.is_element_present(*ShopPageLocators.PRICE_FINAL)
        assert real_price == basket_price, 'hueta'





