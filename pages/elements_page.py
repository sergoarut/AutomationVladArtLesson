import base64
import os
import random
import sys
import time
import requests
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesPageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person, generator_file
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


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


class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    def add_user_in_the_tabel(self, count=1):
        all_person: list = []
        while count != 0:
            person_info = next(generated_person())
            if len(person_info.department) >= 25:
                while len(person_info.department) >= 25:
                    person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            age = person_info.age
            email = person_info.email
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_NEW_USER_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_FORM).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_FORM).send_keys(last_name)
            self.element_is_visible(self.locators.USER_EMAIL_FORM).send_keys(email)
            self.element_is_visible(self.locators.USER_AGE_FORM).send_keys(age)
            self.element_is_visible(self.locators.USER_SALARY_FORM).send_keys(salary)
            self.element_is_visible(self.locators.USER_DEPARTMENT_FORM).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_FORM_BUTTON).click()
            count -= 1
            all_person.append([first_name, last_name, str(age), email, str(salary), department])
        return all_person

    def full_person_in_the_table(self):
        people_list = self.elements_are_presents(self.locators.PRESENT_PERSON)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_people(self, key_word):
        time.sleep(1)
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(1)

    def check_search_person(self):
        return self.element_is_visible(self.locators.PRESENT_PERSON).text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        if len(person_info.department) >= 25:
            while len(person_info.department) >= 25:
                person_info = next(generated_person())
        data_person = {"first_name": person_info.first_name,
                       "last_name": person_info.last_name,
                       "age": person_info.age,
                       "email": person_info.email,
                       "salary": person_info.salary,
                       "department": person_info.department}
        locations_data = {"first_name": self.locators.FIRST_NAME_FORM,
                          "last_name": self.locators.LAST_NAME_FORM,
                          "age": self.locators.USER_AGE_FORM,
                          "email": self.locators.USER_EMAIL_FORM,
                          "salary": self.locators.USER_SALARY_FORM,
                          "department": self.locators.USER_DEPARTMENT_FORM}

        list_keys_data = list(data_person.keys())
        choices_keys = random.choice(list_keys_data)

        list_edit_person = self.elements_are_visible(self.locators.EDIT_PERSON)
        random.choice(list_edit_person).click()

        self.element_is_visible(locations_data[choices_keys]).send_keys(Keys.CONTROL + "A")
        self.element_is_visible(locations_data[choices_keys]).send_keys(Keys.BACKSPACE)
        self.element_is_visible(locations_data[choices_keys]).send_keys(data_person[choices_keys])

        self.element_is_visible(self.locators.SUBMIT_FORM_BUTTON).click()

        return data_person[choices_keys]

    def delete_person(self):
        present_persons = self.elements_are_visible(self.locators.PRESENT_PERSON)
        number_of_people = len(present_persons)
        number_delete_person = random.randint(1, number_of_people)
        delete_person = self.elements_are_presents(self.locators.PRESENT_PERSON)[
            number_delete_person - 1].text.splitlines()
        self.elements_are_visible(self.locators.DELETE_BUTTON)[number_delete_person - 1].click()
        return delete_person

    def change_rows(self):
        locations_rows = {5: self.locators.FIVE_ROWS,
                          10: self.locators.TEN_ROWS,
                          20: self.locators.TWENTY_ROWS,
                          25: self.locators.TWENTY_FIVE_ROWS,
                          50: self.locators.FIVE_ROWS,
                          100: self.locators.ONE_HUNDRED_ROWS}
        counts = [5, 10, 20]
        data = []
        for item in counts:
            count_row_button = self.element_is_visible(self.locators.SELECT_ROWS)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible(locations_rows[item]).click()
            data.append(self.all_rows())
        return data

    def all_rows(self):
        return len(self.elements_are_visible(self.locators.FULL_PEOPLE_LIST))


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def double_click(self):
        self.actions.double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)).perform()

    def check_double_click(self):
        return self.element_is_present(self.locators.DOUBLE_CLICK_MESSAGE).text

    def right_click(self):
        self.actions.context_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)).perform()

    def check_right_click(self):
        return self.element_is_present(self.locators.RIGHT_CLICK_MESSAGE).text

    def dynamic_click(self):
        self.actions.click(self.element_is_visible(self.locators.DYNAMIC_CLICK_BUTTON)).perform()

    def check_dynamic_click(self):
        return self.element_is_present(self.locators.DYNAMIC_CLICK_MESSAGE).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_link(self):
        simple_link = self.element_is_visible(self.locators.DYNAMIC_REQUEST)
        links_href = simple_link.get_attribute('href')
        request = requests.get(links_href)
        if request.status_code == 200:
            simple_link.click()
            self.switch_to_number_tab(2)
            url = self.get_url()
            return links_href, url
        else:
            return links_href, request.status_code

    def check_send_api_link(self):
        current_url = "https://demoqa.com/"
        list_locators = [self.locators.CREATED_REQUEST, self.locators.NO_CONTENT_REQUEST, self.locators.MOVED_REQUEST,
                         self.locators.BED_REQUEST, self.locators.UNAUTHORIZED_REQUEST, self.locators.FORBIDDEN_REQUEST,
                         self.locators.NOT_FOUND_REQUEST]
        status_codes = []
        for link_locator in list_locators:
            link = f"{current_url}{self.element_is_visible(link_locator).get_attribute('id')}"
            status_codes.append(requests.get(link).status_code)
        return status_codes


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        file_path = generator_file()
        self.element_is_present(self.locators.UPLOAD_FILE_BUTTON).send_keys(file_path)
        os.remove(file_path)
        fake_path = 'C:\\fakepath\\' + file_path.split('\\')[-1]
        return fake_path

    def check_uploaded_file(self):
        return self.element_is_visible(self.locators.UPLOADED_TEXT).text

    def download_file(self):
        link = self.element_is_visible(self.locators.DOWNLOAD_FILE_BUTTON).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = sys.path[1] + fr"\downloaded_files\download_file.jpeg"
        with open(path_name_file, "wb+") as file:
            offset = link_b.find(b"\xff\xd8")
            file.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
        os.remove(path_name_file)
        return check_file
