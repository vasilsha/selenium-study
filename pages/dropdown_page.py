from selenium.webdriver.common.by import By

from universal_ui.universal_ui_actions import UniAct


class DropDownPage(UniAct):
    def __init__(self, driver):
        super().__init__(driver)

# ===============================================================================================
    """ GENERAL ACTION"""

    def get_dropdown_page_title(self, title):
        return self._check_page_title(title)


    # =========================================================================================
    """ SINGLE DAY SELECTOR"""

    SELECT_LIST_DEMO_HEADER = (By.XPATH, f"//div[text()='Select List Demo']")
    DROPDOWN_LIST = (By.ID, "select-demo")
    DAY_SELECTED = (By.CLASS_NAME, "selected-value")
    dropdown_list_validators = [SELECT_LIST_DEMO_HEADER, DROPDOWN_LIST]

    def select_list_validation(self):
        return self._validate_multi_visible(self.dropdown_list_validators)

    def select_from_dropdown_list(self, day):
        selected_day = (By.CSS_SELECTOR, f'#select-demo > option:nth-child({day})')
        self._click_single_item(self.DROPDOWN_LIST)
        self._click_single_item(selected_day)
        return self._get_element_text(self.DAY_SELECTED).split("- ")[1]

    # =========================================================================================
    """ MULTI DAY SELECTOR"""

    MULTI_SELECT_HEADER = (By.XPATH, f"//div[text()='Multi Select List Demo']")
    FIRST_SELECTED_BUTTON = (By.CSS_SELECTOR, "#printMe")
    GET_ALL_SELECTED_BUTTON = (By.CSS_SELECTOR, "#printAll")
    SHOW_SELECTED = (By.CLASS_NAME, "getall-selected")
    MULTI_LIST_LOCATOR = (By.CSS_SELECTOR, '#multi-select')
    MULTI_SELECT_LOCATORS = [MULTI_SELECT_HEADER, FIRST_SELECTED_BUTTON,MULTI_LIST_LOCATOR, GET_ALL_SELECTED_BUTTON]

    def multi_list_validation(self):
        return self._validate_multi_visible(self.MULTI_SELECT_LOCATORS)

    def validate_one_city_selected(self):
        if not self._validate_single_visible(self.SHOW_SELECTED):
            return False
        message = self._get_element_text(self.SHOW_SELECTED).split(' : ')
        town = message[1]
        return town

    def single_city_selection(self, city, list_drop):
        selected_city = (By.CSS_SELECTOR, f"#multi-select > option:nth-child({city})")
        self._click_single_item(selected_city)
        self._click_single_item(self.FIRST_SELECTED_BUTTON)
        first_selected_button_status = self.validate_one_city_selected()
        self._click_single_item(self.GET_ALL_SELECTED_BUTTON)
        get_all_selected_status = self.validate_one_city_selected()
        if first_selected_button_status == list_drop[city-1] and get_all_selected_status == list_drop[city-1]:
            return True
        else:
            return False

    def multi_city_selection(self, city_list, city_id):
        element_list = []
        for i in range(len(city_list)):
            city_element = (By.XPATH, f'//*[@id="multi-select"]/option[{city_id[i]+1}]')
            element_list.append(city_element)
        self._click_multiple_items(element_list)
        self._click_single_item(self.FIRST_SELECTED_BUTTON)
        first_selected_city = self.validate_one_city_selected()
        if first_selected_city != city_list[0]:
            return False
        self._click_single_item(self.GET_ALL_SELECTED_BUTTON)
        city_str = ','.join(city_list)
        result = self.validate_multi_city_selected(city_str)
        return result

    def validate_multi_city_selected(self, city_str):
        if not self._validate_single_visible(self.SHOW_SELECTED):
            return False
        displayed_states = self._get_element_text(self.SHOW_SELECTED)
        temp_city_list = displayed_states.split(' : ')
        temp_city_list.pop(0)
        temp_city_str = ','.join(temp_city_list)
        if temp_city_str == city_str:
            return True
        return False
