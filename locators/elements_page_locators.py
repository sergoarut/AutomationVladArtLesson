from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # FORM FIELDS
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    USER_EMAIL = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress.form-control")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress.form-control")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    # CREATE FORM
    OUTPUT_NAME = (By.CSS_SELECTOR, "#name")
    OUTPUT_USER_EMAIL = (By.CSS_SELECTOR, "#email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPEND_LIST_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, ".rct-title")
    CLICKED_ITEM_LIST = (By.XPATH, "//*[@class='rct-icon rct-icon-check']/../../*[@class='rct-title']")
    RECEIVED_ITEMS_LIST = (By.CSS_SELECTOR, ".text-success")


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.XPATH, "//label[@for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.XPATH, "//label[@for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, ".text-success")
