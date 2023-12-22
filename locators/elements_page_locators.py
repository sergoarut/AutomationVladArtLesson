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