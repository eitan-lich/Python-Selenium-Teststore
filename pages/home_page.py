
from pages.base_page import BasePage
from pages.results_page import ResultsPage
from utils.locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    def search_item(self, item) -> ResultsPage:
        self.type_and_enter(self.locators.SEARCH_BAR, item)
        return ResultsPage(self.driver)

