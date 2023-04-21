from pages.base_page import BasePage
from pages.order_page import OrderPage
from utils.locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocators()

    def checkout(self) -> OrderPage:
        self.click(self.locators.CHECKOUT_BUTTON)
        return OrderPage(self.driver)