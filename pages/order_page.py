from pages.base_page import BasePage
from utils.locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def fill_form(self, title, first_name, last_name, email):
        if title == "MR":
            self.click(self.locators.SOCIAL_TITLE_MR)
        elif title == "MS":
            self.click(self.locators.SOCIAL_TITLE_MS)

        self.type(self.locators.FIRST_NAME, first_name)
        self.type(self.locators.LAST_NAME, last_name)
        self.type(self.locators.EMAIL, email)
        self.click(self.locators.AGREE_TERMS)
        self.click(self.locators.CONTINUE_BUTTON)


