from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage


class BaseTest:
    def setUp(self):
        options = Options()
        options.add_argument('--start-maximized')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://teststore.automationtesting.co.uk/")






if __name__ == "__main__":
    options = Options()
    options.add_argument('--started-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get("http://teststore.automationtesting.co.uk/")
    home_page = HomePage(driver)
    home_page.search_item("t-shirt")


