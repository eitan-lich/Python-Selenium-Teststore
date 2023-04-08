from pages.base_page import BasePage
from pages.item_page import ItemPage
from utils.locators import ResultPageLocators


class ResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ResultPageLocators()

    def click_first_item(self):
        self.click(self.locators.FIRST_ITEM)
        return ItemPage(self.driver)