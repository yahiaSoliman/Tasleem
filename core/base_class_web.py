import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BaseClassWeb(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Start browser maximized
        chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
        chrome_options.add_argument("--no-sandbox")
        chrome_options.executable_path = 'D:\projects\Tasleem automation py\chromedriver.exe'

        # Initializing the Chrome driver
        self.driver = webdriver.Chrome(chrome_options)

        # Implicit wait
        self.driver.implicitly_wait(20)

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()
