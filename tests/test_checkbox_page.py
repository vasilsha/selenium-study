
import unittest

from pages.checkbox_page import CheckboxPage
from selenium import webdriver


class TestCheckboxPage(unittest.TestCase):
    url = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"

    def setUp(self):
        """ Setup test environment """
        print("setUp")
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.checkbox_page = CheckboxPage(self.driver)
            self.assertTrue(self.driver.current_url == self.url, "The current URL is not the URL that is required!")
        except Exception:
            raise Exception("Unable to verify homepage URL.")

    def tearDown(self):
        print("teardown")
        self.driver.close()
        self.driver.quit()

    def test_01_checkbox_page_title(self):
        """ Test to make sure the correct title is displayed"""
        is_it = self.checkbox_page.get_checkbox_page_title('Selenium Easy')
        self.assertTrue(is_it)

    def test_02_single_checkbox(self):
        """ Test to make sure the checkbox activate message"""
        is_visible = self.checkbox_page.select_checkbox_validation()
        self.assertTrue(is_visible)
        self.assertEqual(self.checkbox_page.select_single_checkbox(), 'Success - Check box is checked')

    def test_03_multiple_checkbox(self):
        is_visible = self.checkbox_page.multi_checkbox_validation()
        self.assertTrue(is_visible)
        self.assertTrue(self.checkbox_page.multi_checkbox_select())


