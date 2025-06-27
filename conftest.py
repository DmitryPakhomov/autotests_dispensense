import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config import LOGIN, PASSWORD
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests with browser UI (headed mode)"
    )


@pytest.fixture(scope="function")
def driver(request):
    # Получаем значение флага --headed
    headed = request.config.getoption("--headed")

    options = Options()
    if not headed:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    login_page = LoginPage(driver)
    login_page.login(email=LOGIN, password=PASSWORD)
    login_page.should_see_username()
    return login_page
