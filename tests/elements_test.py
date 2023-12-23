import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage


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
            assert permanent_address == output_per_addr , "the permanent address does not match"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            clicket_items = check_box_page.get_clicked_items()
            received_items = check_box_page.get_received_items()
            assert clicket_items == received_items, "clicked items are not equal to received items"


