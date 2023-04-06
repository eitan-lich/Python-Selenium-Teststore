import unittest

from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from tests.base_test import BaseTest


class SearchItem(BaseTest):
    def test_search_item(self):
        home_page = HomePage(self.driver)
        home_page.search_item("t-shirt")
        tshirt = self.driver.find_element(By.CSS_SELECTOR, ".h3.product-title > a").text
        self.assertIn("Hummingbird Printed T-Shirt", tshirt)





if __name__ == "__main__":
    unittest.main()