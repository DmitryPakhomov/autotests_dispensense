import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config import LOGIN, PASSWORD
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    #options.add_argument("--headless=new")  # для безголового запуска браузера
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
