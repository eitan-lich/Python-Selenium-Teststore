import unittest

from pages.home_page import HomePage
from tests.base_test import BaseTest


class SearchItem(BaseTest):
    def test_search_item(self):
        home_page = HomePage(self.driver)
        item_name = "mug"
        results_page = home_page.search_item(item_name)
        self.assertTrue(results_page.check_item_exist(item_name))

if __name__ == "__main__":
    unittest.main()