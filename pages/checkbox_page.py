from selenium.webdriver.common.by import By
from universal_ui.universal_ui_actions import UniAct


class CheckboxPage(UniAct):
    def __init__(self, driver):
        super().__init__(driver)

    # ===============================================================================================
    """ GENERAL ACTION"""

    def get_checkbox_page_title(self, title):
        return self._check_page_title(title)

    # ==============================================================================================
    """SINGLE CHECKBOX"""
    SINGLE_CHECKBOX_HEADER = (By.CSS_SELECTOR, 'div.panel:nth-child(4) > div:nth-child(1)')
    SINGLE_CHECKBOX_ELEMENT = (By.CSS_SELECTOR, '#isAgeSelected')
    SINGLE_CHECKBOX_MESSAGE = (By.CSS_SELECTOR, '#txtAge')
    SINGLE_CHECKBOX_VALIDATOR = (SINGLE_CHECKBOX_HEADER, SINGLE_CHECKBOX_ELEMENT)

    def select_checkbox_validation(self):
        return self._validate_multi_visible(self.SINGLE_CHECKBOX_VALIDATOR)

    def select_single_checkbox(self):
        self._click_single_item(self.SINGLE_CHECKBOX_ELEMENT)
        return self._get_element_text(self.SINGLE_CHECKBOX_MESSAGE)

    # ==============================================================================================
    """MULTIPLE CHECKBOX"""
    MULTIPLE_CHECKBOX_HEADER = (
        By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-heading')
    MULTIPLE_CHECKBOX_FIRST = (By.CSS_SELECTOR,
                               '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > div:nth-child(3) > label > input')
    MULTIPLE_CHECKBOX_SECOND = (By.CSS_SELECTOR,
                                '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > div:nth-child(4) > label > input')
    MULTIPLE_CHECKBOX_THIRD = (By.CSS_SELECTOR,
                               '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > div:nth-child(5) > label > input')
    MULTIPLE_CHECKBOX_FOURTH = (By.CSS_SELECTOR,
                                '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > div.panel-body > div:nth-child(6) > label > input')
    MULTIPLE_CHECKBOX_CLICKABLE = (By.CSS_SELECTOR, '#check1')
    MULTIPLE_CHECKBOX_IS_CHECKED = (By.CSS_SELECTOR, '#isChkd')
    MULTIPLE_CHECKBOX_VALIDATOR = (
        MULTIPLE_CHECKBOX_HEADER, MULTIPLE_CHECKBOX_FIRST, MULTIPLE_CHECKBOX_SECOND, MULTIPLE_CHECKBOX_THIRD,
        MULTIPLE_CHECKBOX_FOURTH, MULTIPLE_CHECKBOX_CLICKABLE)

    def multi_checkbox_validation(self):
        return self._validate_multi_visible(self.MULTIPLE_CHECKBOX_VALIDATOR)

    def multi_checkbox_select(self):
        # click checkboxes and compare the flag status
        self._click_single_item(self.MULTIPLE_CHECKBOX_FIRST)
        element = self._get_invisible_element(self.MULTIPLE_CHECKBOX_IS_CHECKED)
        if element.get_property('value') == 'true':
            return False
        self._click_single_item(self.MULTIPLE_CHECKBOX_SECOND)
        element = self._get_invisible_element(self.MULTIPLE_CHECKBOX_IS_CHECKED)
        if element.get_property('value') == 'true':
            return False
        self._click_single_item(self.MULTIPLE_CHECKBOX_THIRD)
        element = self._get_invisible_element(self.MULTIPLE_CHECKBOX_IS_CHECKED)
        if element.get_property('value') == 'true':
            return False
        self._click_single_item(self.MULTIPLE_CHECKBOX_FOURTH)
        element = self._get_invisible_element(self.MULTIPLE_CHECKBOX_IS_CHECKED)
        # all checked now
        if element.get_property('value') == 'false':
            return False
        self._click_single_item(self.MULTIPLE_CHECKBOX_CLICKABLE)
        element = self._get_invisible_element(self.MULTIPLE_CHECKBOX_IS_CHECKED)
        # all unchecked
        if element.get_property('value') == 'true':
            return False
        self._click_single_item(self.MULTIPLE_CHECKBOX_CLICKABLE)
        element = self._get_invisible_element(self.MULTIPLE_CHECKBOX_IS_CHECKED)
        # all checked again
        if element.get_property('value') == 'false':
            return False
        return True
