import random
import time

import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage


class TestElements:
    class TestTextBox:

        @pytest.mark.skip
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_curr_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent address does not match"

    class TestCheckBox:

        @pytest.mark.skip
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            clicket_items = check_box_page.get_clicked_items()
            received_items = check_box_page.get_received_items()
            assert clicket_items == received_items, "clicked checkbox are not equal to received checkbox"

    class TestRadioButton:

        @pytest.mark.skip
        def test_radiobutton(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            key = ["Yes", "Impressive", "No"]
            radio_button_page.click_on_the_radiobutton(key[0])
            received_yes_radio_button = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radiobutton(key[1])
            received_impressive_radio_button = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radiobutton(key[2])
            received_no_radio_button = radio_button_page.get_output_result()
            assert key[0] == received_yes_radio_button, "'Yes' radiobutton are not equal to received radiobutton"
            assert key[1] == received_impressive_radio_button, "'Impressive' radiobutton are not equal " \
                                                               "to received radiobutton"
            # assert key[2] == received_no_radio_button, "'No' radiobutton are not equal to received radiobutton"
            """"Бага сервиса, данная кнопка задизейблена"""

    class TestWebTables:
        @pytest.mark.skip
        def test_web_tables_add_person(self, driver):
            web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables_page.open()
            namber_added_people = random.randint(1, 7)
            added_person_list = web_tables_page.add_user_in_the_tabel(namber_added_people)
            all_person_list = web_tables_page.full_person_in_the_table()
            for person in added_person_list:
                assert person in all_person_list, "Added person is not in the table"

        @pytest.mark.skip
        def test_web_table_search_person(self, driver):
            web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables_page.open()
            namber_added_people = random.randint(1, 7)
            web_tables_page.add_user_in_the_tabel(namber_added_people)
            full_list = web_tables_page.full_person_in_the_table()
            key_word_search = random.choice(random.choice(full_list))
            web_tables_page.search_some_people(key_word_search)
            search_results = web_tables_page.check_search_person()
            print(str(key_word_search))
            print(search_results)
            assert any(str(key_word_search) in str(item) for item in search_results), \
                "The search person was not found in thetable"

        @pytest.mark.skip
        def test_web_table_update_person_info(self, driver):
            web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables_page.open()
            namber_added_people = random.randint(1, 7)
            web_tables_page.add_user_in_the_tabel(namber_added_people)
            changed_valeu = web_tables_page.update_person_info()
            web_tables_page.search_some_people(changed_valeu)
            search_results = web_tables_page.check_search_person()
            print(str(changed_valeu))
            print(search_results)
            assert any(str(changed_valeu) in str(item) for item in search_results), \
                "The changed person was not found in thetable"

        @pytest.mark.skip
        def test_web_tables_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables_page.open()
            namber_added_people = random.randint(1, 7)
            web_tables_page.add_user_in_the_tabel(namber_added_people)
            delete_person = web_tables_page.delete_person()
            all_person = web_tables_page.full_person_in_the_table()
            assert delete_person not in all_person, "Delete person in the table"

        @pytest.mark.skip
        def test_web_tables_change_rows_table(self, driver):
            web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
            web_tables_page.open()
            count = [5, 10, 20]
            rows_list = web_tables_page.change_rows()
            assert rows_list == count, 'The number of rows in the table has not been changed or has changed incorrectly'
            # на странице баг в верстке при попытке открыть 25, 50, 100 строк
