import unittest
import random
from pages.dropdown_page import DropDownPage
from selenium import webdriver


class TestDropdownPage(unittest.TestCase):
    url = "https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html"
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    states = ["California", "Florida", "New Jersey", "New York", "Ohio", "Texas", "Pennsylvania", "Washington"]

    def setUp(self):
        """ Setup test environment """
        print("setUp")
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.dropdown_page = DropDownPage(self.driver)
            self.assertTrue(self.driver.current_url == self.url, "The current URL is not the URL that is required!")
        except Exception:
            raise Exception("Unable to verify homepage URL.")

    def tearDown(self):
        print("teardown")
        self.driver.close()
        self.driver.quit()

    def test_01_dropdown_page_title(self):
        """ Test to make sure the correct title is displayed"""
        is_it = self.dropdown_page.get_dropdown_page_title('Selenium Easy')
        self.assertTrue(is_it)

    def test_02_select_list_demo(self):
        """ test the functionality of the single list field section"""
        items_visible = self.dropdown_page.select_list_validation()
        self.assertTrue(items_visible)
        num_choice = [2, 3, 4, 5, 6, 7, 8]
        num = random.choice(num_choice)
        dict_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        retrieved_message = self.dropdown_page.select_from_dropdown_list(num)
        self.assertEqual(retrieved_message, dict_list[num - 2])

    def test_03_select_one_city_selection(self):
        """ test the functionality of the multi list fields section"""
        num_list_choice = [1, 2, 3, 4, 5, 6, 7, 8]
        num_choice = random.choice(num_list_choice)
        list_drop = ['California', 'Florida', 'New Jersey', 'New York', 'Ohio', 'Texas', 'Pennsylvania', 'Washington']
        items_visible = self.dropdown_page.multi_list_validation()
        self.assertTrue(items_visible)
        is_it = self.dropdown_page.single_city_selection(num_choice, list_drop)
        self.assertTrue(is_it)

    def test_04_select_multi_city_selection(self):
        """ test the functionality of the multi list fields section"""
        list_drop = ['California', 'Florida', 'New Jersey', 'New York', 'Ohio', 'Texas', 'Pennsylvania', 'Washington']
        city_list = []
        city_id = []
        while len(city_list) <= 1:
            city_list = []
            for i in range(len(list_drop)):
                if random.randint(0, 1) == 1:
                    city_list.append(list_drop[i])
                    city_id.append(i)
        items_visible = self.dropdown_page.multi_list_validation()
        self.assertTrue(items_visible)
        is_it = self.dropdown_page.multi_city_selection(city_list, city_id)
        self.assertTrue(is_it)
