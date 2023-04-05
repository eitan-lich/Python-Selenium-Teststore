
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(locator)

    def click(self, locator):
        return self.find(locator).click()

    def get_url(self):
        return self.url

    def get_title(self):
        return self.driver.title