import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TenantPage:
    NAME_INPUT = (By.ID, "tenantName")
    DESCRIPTION_INPUT = (By.ID, "tenantDescription")
    SAVE_BUTTON = (By.ID, "saveButton")
    SUCCESS_MESSAGE = (By.ID, "notificationMessage")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def clear_and_type(self, element, value: str):
        """Универсальный метод очистки поля и ввода текста"""
        try:
            element.clear()
        except Exception:
            pass
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(value)


    def open(self):
        """Открыть страницу Tenant (раздел Organisation в Management)"""
        pass

    def set_name(self, name: str):
        name_field = self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT))
        self.clear_and_type(name_field, name)

    def set_description(self, description: str):
        description_field = self.wait.until(EC.visibility_of_element_located(self.DESCRIPTION_INPUT))
        self.clear_and_type(description_field, description)

    def save_changes(self):
        save_btn = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_btn.click()

    def should_see_success_message(self, expected: str = "Organisation was updated"):
        message = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        assert expected in message.text, f"Expected message '{expected}', but got '{message.text}'"

    def should_have_name(self, expected_name: str):
        """Проверить, что имя организации соответствует ожидаемому"""
        name_input = self.wait.until(EC.presence_of_element_located(self.NAME_INPUT))
        actual = name_input.get_attribute("value").strip()
        assert actual == expected_name, f"Expected name '{expected_name}', but got '{actual}'"

    def should_have_description(self, expected_description: str):
        """Проверить, что описание соответствует ожидаемому"""
        desc_input = self.wait.until(EC.presence_of_element_located(self.DESCRIPTION_INPUT))
        actual = desc_input.get_attribute("value").strip()
        assert actual == expected_description, f"Expected description '{expected_description}', but got '{actual}'"

    def should_see_field_error(self, field: str, message: str = "This field is required"):
        """
        Проверить, что под указанным полем отображается сообщение об ошибке.
        :param field: идентификатор поля, например 'tenantName'
        :param message: ожидаемое сообщение
        """
        error_locator = (By.ID, f"{field}-messages")
        error_block = self.wait.until(EC.visibility_of_element_located(error_locator))
        assert message in error_block.text, f"Expected error message '{message}', but got '{error_block.text}'"

    def get_tenant_info(self) -> tuple[str, str]:
        """Получить имя и описание организации с формы"""
        name_input = self.wait.until(EC.presence_of_element_located(self.NAME_INPUT))
        name = name_input.get_attribute("value").strip()
        desc_input = self.wait.until(EC.presence_of_element_located(self.DESCRIPTION_INPUT))
        description = desc_input.get_attribute("value").strip()

        return name, description
