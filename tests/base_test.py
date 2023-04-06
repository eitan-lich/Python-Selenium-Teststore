from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--start-maximized')
        config = configparser.ConfigParser()
        config.read('../utils/configuration.ini')

        if config['selenium']['browser'] == "chrome":
            self.driver = webdriver.Chrome(options=options)

        url=config['selenium']['url']
        self.driver.get(url)

    def tearDown(self):
        print("im tearing down the session now!")
        self.driver.quit()



