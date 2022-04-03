import random
import unittest
from pages.complex_form_page import ComplexFormPage
from selenium import webdriver


class TestDropdownPage(unittest.TestCase):
    url = "https://www.seleniumeasy.com/test/input-form-demo.html"

    def setUp(self):
        """ Setup test environment """
        print("setUp")
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.complex_form_page = ComplexFormPage(self.driver)
            self.assertTrue(self.driver.current_url == self.url, "The current URL is not the URL that is required!")
        except Exception:
            raise Exception("Unable to verify homepage URL.")

    def tearDown(self):
        print("teardown")
        self.driver.close()
        self.driver.quit()

    def test_01_complex_form_page_title(self):
        """ Test to make sure the correct title is displayed"""
        is_it = self.complex_form_page.get_complex_form_page_title('Selenium Easy')
        self.assertTrue(is_it)

    def test_02_complex_form_page_fail_test(self):
        """ Test that all fail messages are displayed"""
        is_it = self.complex_form_page.select_complex_form_validation()
        self.assertTrue(is_it)
        is_it = self.complex_form_page.select_complex_form_fill_fail()
        self.assertTrue(is_it)

    def test_03_complex_form_page_success_test(self):
        """ Test that no fail messages is displayed"""
        account_details = ['Azxcvbnm', 'test@t', '0123456789', '012345678']
        yes_no = random.randint(0, 1)
        account_details.append(yes_no)
        state = random.randint(2, 52)
        account_details.append(state)
        is_it = self.complex_form_page.select_complex_form_validation()
        self.assertTrue(is_it)
        is_it = self.complex_form_page.select_complex_form_fill_success(account_details)
        self.assertTrue(is_it)
