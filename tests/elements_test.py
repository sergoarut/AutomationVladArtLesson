import random
import time

import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


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

    class TestButtons:

        @pytest.mark.skip
        def test_double_click_botton(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            buttons_page.double_click()
            expected_message = "You have done a double click"
            message = buttons_page.check_double_click()
            assert message == expected_message, "The double click did not occure"

        @pytest.mark.skip
        def test_right_click_botton(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            buttons_page.right_click()
            expected_message = "You have done a right click"
            message = buttons_page.check_right_click()
            assert message == expected_message, "The right click did not occure"

        @pytest.mark.skip
        def test_dynamic_click_botton(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            buttons_page.dynamic_click()
            expected_message = "You have done a dynamic click"
            message = buttons_page.check_dynamic_click()
            assert message == expected_message, "The dynamic click did not occure"

    class TestLinks:

        @pytest.mark.skip
        def test_check_link_open_tab(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_url, current_url = links_page.check_new_tab_link()
            assert href_url == current_url, "Status code are not equal to 200"

        @pytest.mark.skip
        def test_send_api_links(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            required_status_codes = [201, 204, 301, 400, 401, 403, 404]
            recived_status_codes = links_page.check_send_api_link()
            assert recived_status_codes == required_status_codes, "Status codes are not equal to required status codes"

    class TestUploadAndDownload:

        @pytest.mark.skip
        def test_upload_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_page.open()
            upload_file_path = upload_page.upload_file()
            uploaded_path = upload_page.check_uploaded_file()
            assert uploaded_path == upload_file_path, "Failed to uploaded file"

        @pytest.mark.skip
        def test_download_file(self, driver):
            download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            download_page.open()
            check = download_page.download_file()
            assert check == True, "Failed to downloaded file"

    class TestDynamicProperties:

        @pytest.mark.skip
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            clickable = dynamic_properties_page.check_enable_button()
            assert clickable == True, 'Element of not clicable'

        @pytest.mark.skip
        def test_change_color_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            red_color = 'rgba(220, 53, 69, 1)'
            color_before, color_after = dynamic_properties_page.check_change_of_color()
            assert color_before == red_color, 'Element of not red color'

        @pytest.mark.skip
        def test_visible_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            visible = dynamic_properties_page.check_visible_button()
            assert visible == True, 'Element of not visibled in 5 second'
