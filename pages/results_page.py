from pages.base_page import BasePage
from pages.item_page import ItemPage
from utils.locators import ResultPageLocators


class ResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ResultPageLocators()

    def click_first_item(self) -> ItemPage:
        self.click(self.locators.FIRST_ITEM)
        return ItemPage(self.driver)

    def check_item_exist(self, item_name) -> bool:
        item_list = self.find_multiple(self.locators.PRODUCT_LIST)
        if len(item_list) == 0:
            return False

        for item in item_list:
            if item_name in item.text.lower():
                return True

        return False


