from selenium.webdriver import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def get_url(self):
        return self.url

    def type(self, locator, text):
        print(locator)
        self.find(locator).send_keys(text)

    def type_and_enter(self, locator, text):
        self.find(locator).send_keys(text)
        self.find(locator).send_keys(Keys.ENTER)

    def get_title(self):
        return self.driver.title
