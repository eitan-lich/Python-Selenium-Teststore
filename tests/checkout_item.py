import time

from pages.home_page import HomePage
from tests.base_test import BaseTest


class CheckoutItem(BaseTest):

    def test_checkout_item_valid(self):
        homepage = HomePage(self.driver)
        results_page = homepage.search_item("t-shirt")
        time.sleep(2)
        item_page = results_page.click_first_item()
        item_page.add_to_cart()
        cart_page = item_page.click_on_cart()
        order_page = cart_page.checkout()
        order_page.fill_form("MR", "Eitan", "Lichtenstein", "eitanlich2000@gmail.com")
        input()









