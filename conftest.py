import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument(r"--user-data-dir=C:\Users\Сережа\PycharmProjects\AutomationVladArtLesson\chrome")
    options.add_argument("--user-agen5t='Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    service = Service(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
