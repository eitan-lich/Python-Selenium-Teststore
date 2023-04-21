import time

from pages.base_page import BasePage
from pages.cart_page import CartPage
from utils.locators import ItemPageLocators


class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ItemPageLocators()

    def add_to_cart(self):
        self.click(self.locators.ADD_CART_BUTTON)
        time.sleep(2)
        self.click(self.locators.CLOSE_POPUP)

    def click_on_cart(self) -> CartPage:
        self.click(self.locators.CART_BUTTON)
        return CartPage(self.driver)