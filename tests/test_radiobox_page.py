import unittest

from pages.radiobox_page import RadioPage
from selenium import webdriver


class TestCheckboxPage(unittest.TestCase):
    url = "https://www.seleniumeasy.com/test/basic-radiobutton-demo.html"

    def setUp(self):
        """ Setup test environment """
        print("setUp")
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.radiobox_page = RadioPage(self.driver)
            self.assertTrue(self.driver.current_url == self.url, "The current URL is not the URL that is required!")
        except Exception:
            raise Exception("Unable to verify homepage URL.")

    def tearDown(self):
        print("teardown")
        self.driver.close()
        self.driver.quit()

    def test_01_radio_page_title(self):
        """ Test to make sure the correct title is displayed"""
        is_it = self.radiobox_page.get_checkbox_page_title('Selenium Easy')
        self.assertTrue(is_it)

    def test_02_single_radio(self):
        """ Test the single radio selection """
        is_visible = self.radiobox_page.select_single_radio_validation()
        self.assertTrue(is_visible)
        self.assertTrue(self.radiobox_page.select_single_radio())

    def test_03_multiple_radio(self):
        """ Test the multiple radio selection """
        is_visible = self.radiobox_page.select_multiple_radio_validation()
        self.assertTrue(is_visible)
        self.assertTrue(self.radiobox_page.select_multiple_radio())
