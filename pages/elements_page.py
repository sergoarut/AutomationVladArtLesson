import random

from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.USER_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.OUTPUT_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.OUTPUT_USER_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPEND_LIST_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 25
        while count != 0:
            item = item_list[random.randint(0, 16)]
            self.go_to_element(item)
            item.click()
            count -= 1

    def get_clicked_items(self):
        list_clicked_checkbox = []
        clicked_checkbox = self.elements_are_presents(self.locators.CLICKED_ITEM_LIST)
        for item in clicked_checkbox:
            list_clicked_checkbox.append(item.text.lower().split('.')[0].replace(" ", ""))
        return list_clicked_checkbox

    def get_received_items(self):
        list_received_checkbox = []
        received_checkbox = self.elements_are_visible(self.locators.RECEIVED_ITEMS_LIST)
        for item in received_checkbox:
            list_received_checkbox.append(item.text.lower().split('.')[0].replace(" ", ""))
        return list_received_checkbox


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radiobutton(self, choice):
        choices = {"Yes": self.locators.YES_RADIO_BUTTON,
                   "Impressive": self.locators.IMPRESSIVE_RADIO_BUTTON,
                   "No": self.locators.NO_RADIO_BUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text
