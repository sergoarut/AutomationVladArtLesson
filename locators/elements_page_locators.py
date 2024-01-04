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


class WebTablesPageLocators:
    # ADD PERSON FORM
    ADD_NEW_USER_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    FIRST_NAME_FORM = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_FORM = (By.CSS_SELECTOR, "#lastName")
    USER_EMAIL_FORM = (By.CSS_SELECTOR, "#userEmail")
    USER_AGE_FORM = (By.CSS_SELECTOR, "#age")
    USER_SALARY_FORM = (By.CSS_SELECTOR, "#salary")
    USER_DEPARTMENT_FORM = (By.CSS_SELECTOR, "#department")
    SUBMIT_FORM_BUTTON = (By.CSS_SELECTOR, "#submit")

    # TABLE
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".input-group-append")
    PRESENT_PERSON = (By.XPATH, "//span[@title='Delete']//ancestor::div[@class='rt-tr-group']")
    EDIT_PERSON = (By.XPATH, "//span[@title='Edit']")
    DELETE_BUTTON = (By.XPATH, "//span[@title='Delete']")

    # ROWS
    SELECT_ROWS = (By.XPATH, "//select[@aria-label='rows per page']")
    FIVE_ROWS = (By.CSS_SELECTOR, "option[value='5']")
    TEN_ROWS = (By.CSS_SELECTOR, "option[value='10']")
    TWENTY_ROWS = (By.CSS_SELECTOR, "option[value='20']")
    TWENTY_FIVE_ROWS = (By.CSS_SELECTOR, "option[value='25']")
    FIFTY_ROWS = (By.CSS_SELECTOR, "option[value='50']")
    ONE_HUNDRED_ROWS = (By.CSS_SELECTOR, "option[value='100']")


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "#doubleClickMessage")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "#rightClickMessage")
    DYNAMIC_CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    DYNAMIC_CLICK_MESSAGE = (By.CSS_SELECTOR, "#dynamicClickMessage")


class LinksPageLocators:
    DYNAMIC_REQUEST = (By.CSS_SELECTOR, "#dynamicLink")
    CREATED_REQUEST = (By.CSS_SELECTOR, "#created")
    NO_CONTENT_REQUEST = (By.CSS_SELECTOR, "#no-content")
    MOVED_REQUEST = (By.CSS_SELECTOR, "#moved")
    BED_REQUEST = (By.CSS_SELECTOR, "#bad-request")
    UNAUTHORIZED_REQUEST = (By.CSS_SELECTOR, "#unauthorized")
    FORBIDDEN_REQUEST = (By.CSS_SELECTOR, "#forbidden")
    NOT_FOUND_REQUEST = (By.CSS_SELECTOR, "#invalid-url")


class UploadAndDownloadPageLocators:
    UPLOAD_FILE_BUTTON = (By.CSS_SELECTOR, "#uploadFile")
    UPLOADED_TEXT = (By.CSS_SELECTOR, "#uploadedFilePath")
    DOWNLOAD_FILE_BUTTON = (By.CSS_SELECTOR, "#downloadButton")


class DynamicPropertiesPageLocators:
    ENABLE_BUTTON = (By.CSS_SELECTOR, "#enableAfter")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "#colorChange")
    VISIBLE_BUTTON = (By.CSS_SELECTOR, "#visibleAfter")

