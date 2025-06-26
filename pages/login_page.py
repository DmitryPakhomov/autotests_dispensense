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

    def should_see_username(self, expected_name: str = "testpharm4 test", timeout: int = 30):
        """Проверка, что имя пользователя отображается после входа"""
        username_locator = (By.XPATH, f"//*[contains(text(), '{expected_name}')]")
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(username_locator)
        )
        assert expected_name in element.text, f"Expected to see '{expected_name}', but saw '{element.text}'"

    def logout(self):
        """Простейший выход — можно улучшить при наличии UI-кнопки logout"""
        self.driver.delete_all_cookies()
