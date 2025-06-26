from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://app.stage.dispensense.ie/"
    EMAIL_INPUT = (By.ID, "emailField")
    PASSWORD_INPUT = (By.ID, "passwordField")
    LOGIN_BUTTON = (By.ID, "loginButton")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, email: str, password: str, timeout: int = 10):
        """Открыть страницу и выполнить вход с заданным таймаутом ожидания"""
        self.driver.get(self.URL)
        wait = WebDriverWait(self.driver, timeout)

        wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def should_see_username(self, expected_name: str = "test pharm4", timeout: int = 60):
        """Проверка, что имя пользователя отображается в блоке #username"""
        name_locator = (By.CSS_SELECTOR, "#username > div:first-child")
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(name_locator)
        )
        actual = element.text.strip()
        assert actual == expected_name, f"Expected username '{expected_name}', but got '{actual}'"

    def logout(self):
        """Простейший выход — можно улучшить при наличии UI-кнопки logout"""
        self.driver.delete_all_cookies()
