from pages.base_page import BasePage
from utils.locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    def search_item(self, item):
        self.find(self.locators.SEARCH_BAR).send_keys(item)

