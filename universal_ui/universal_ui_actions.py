import time

from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class UniAct:
    def __init__(self, driver):
        self.driver = driver

    def _check_page_title(self, title):
        # get driver and part of the title of the page
        # return true or false if it is correct
        return WebDriverWait(self.driver, 10).until(EC.title_contains(title))

    def _validate_single_visible(self, locator):
        # get driver and css selector
        # return true or false
        element_is_visible = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element_is_visible

    def _validate_multi_visible(self, locators_list):
        # get driver and list of css selectors
        # return true or false
        visible = True
        for locator in locators_list:
            element_visible = self._validate_single_visible(locator)
            if not element_visible:
                visible = False
        return visible

    def _click_single_item(self, locator):
        # get driver and css locator
        # click on selected element
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def _click_multiple_items(self, list_locator):
        # get driver and list of css selectors
        # click on all selected modules
        ac = ActionChains(self.driver)
        ac.key_down(Keys.LEFT_CONTROL)
        for locator in list_locator:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            ac.click(element)
        ac.key_up(Keys.LEFT_CONTROL)
        ac.perform()

    def _input_text(self, locator, text):
        # input sent text into an element
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def _get_element_text(self, locator):
        # return text of the visible element
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def _get_invisible_element(self, locator):
        # return invisible element for further work
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))
            return True
        except TimeoutError:
            return False

    def _get_multi_invisible_element(self, locators_list):
        # get driver and list of css selectors
        # return true or false
        for locator in locators_list:
            element_invisible = self._get_invisible_element(locator)
            if not element_invisible:
                return False
        return True

    def _validate_clickable(self, locator, is_selected):
        """NOT FINISHED"""
        # return true if element is c
        is_it = WebDriverWait(self.driver, 10).until(EC.element_located_selection_state_to_be(locator, is_selected))
        return is_it
