import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class PharmacyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # test_data/pharmacy_data.py

    pharmacy_data = {
        "name": "Test Pharmacy",
        "address_line1": "Line 123",
        "address_line2": "Line 456",
        "town": "Dublin",
        "country": "Ireland",
        "eircode": "D15 KC3H",
        "gms": "12345",
        "vat_number": "1234567WA",
        "navi_account": "NAVI-7890",
        "label_type": "Standard",
        "label_font_size": "12",
        "signature_label": "Signature",
        "copy_type": "2",
        "printer_name": "HP-LaserJet",
        "copy_layout": "Horizontal",
        "copy_font_size": "10",
        "copy_label_type": "Prescription"
    }


    # Locators
    # --- Main Info Locators ---
    NAME_INPUT = (By.ID, "nameTextField")
    ADDRESS_LINE1_INPUT = (By.ID, "addressLine1")
    ADDRESS_LINE2_INPUT = (By.ID, "addressLine2")
    TOWN_INPUT = (By.ID, "addressTown")
    COUNTRY_INPUT = (By.ID, "country")
    POSTAL_CODE_INPUT = (By.ID, "postalCode")  # Eircode
    GMS_INPUT = (By.ID, "gmsCodeTextField")
    VAT_INPUT = (By.ID, "vatNumberTextField")
    NAVI_ACCOUNT_INPUT = (By.ID, "naviAccount")
    EIRCODE_INPUT = (By.ID, "addressEirCode")
    SEARCH_INPUT = (By.ID, "searchTextField")

    # --- Group and Save ---
    GROUP_SELECT = (By.ID, "pharmacyGroupsSelect")
    ADD_PHARMACY_BUTTON = (By.ID, "addPharmacyButton")
    SAVE_BUTTON = (By.ID, "saveButton")
    NOTIFICATION = (By.ID, "notificationMessage")
    PHARMACY_GROUP_SELECT_INPUT = (By.ID, "pharmacyGroupsSelect")

    # --- Default Printing Settings ---
    LABEL_PRINTER_SELECT = (By.ID, "defaultLabelPrinter")
    A4_PRINTER_SELECT = (By.ID, "defaultA4Printer")
    RECEIPT_PRINTER_SELECT = (By.ID, "defaultReceiptPrinter")

    # --- supplies ---
    ADD_SUPPLIER_BUTTON = (By.ID, "addSupplierIntegrationButton")
    SUPPLIER_NAME_INPUT = (By.ID, "supplierIntegrationDialogSupplierName")
    PHONE_INPUT = (By.ID, "supplierIntegrationDialogPhone")
    EMAIL_INPUT = (By.ID, "supplierIntegrationDialogEmail")
    ACCOUNT_INPUT = (By.ID, "supplierIntegrationDialogAccountNumber")
    PASSWORD_INPUT = (By.ID, "supplierIntegrationDialogPassword")
    TOGGLE_SWITCH = (By.ID, "supplierIntegrationDialogIntegrationSwitch")
    SAVE_BUTTON_INTEGRATION = (By.ID, "supplierIntegrationDialogSaveButton")

    CONTACT_PHONE_1 =  (By.ID, "phone1TextField")
    CONTACT_PHONE_2 = (By.ID, "phone2TextField")
    CONTACT_EMAIL_1 =  (By.ID, "email1TextField")
    CONTACT_EMAIL_2 = (By.ID, "email2TextField")



    def search(self, text: str):
        """Search for a pharmacy using the search input field"""
        search_field = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)

    def click_add_pharmacy(self):
        """Click on the Add Pharmacy button"""
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_PHARMACY_BUTTON))
        add_button.click()

    def select_pharmacy_group(self):
        """Click on the pharmacy group select input (multi-select)"""
        group_select = self.wait.until(EC.element_to_be_clickable(self.PHARMACY_GROUP_SELECT_INPUT))
        group_select.click()

    def should_see_pharmacy(self, name: str):
        """Verify that the pharmacy name is displayed in the Name field after saving"""
        name_field = self.wait.until(EC.visibility_of_element_located((By.ID, "nameTextField")))
        actual_name = name_field.get_attribute("value")
        assert actual_name == name, f"Expected pharmacy name '{name}', but got '{actual_name}'"

    def should_not_see_pharmacy(self, name: str):
        """Verify that a pharmacy with the specified name is not shown"""
        xpath = f"//tr[contains(@class, 'v-data-table__tr')]//div[contains(text(), '{name}')]"
        self.driver.implicitly_wait(0)
        elements = self.driver.find_elements(By.XPATH, xpath)
        self.driver.implicitly_wait(10)
        assert len(elements) == 0, f"Expected NOT to see pharmacy '{name}', but it was found."

    def get_all_pharmacy_names(self):
        """Return a list of all visible pharmacy names in the table"""
        xpath = "//tr[contains(@class, 'v-data-table__tr')]//div[starts-with(@id, 'pharmacyName_')]"
        elements = self.driver.find_elements(By.XPATH, xpath)
        return [el.text.strip() for el in elements if el.text.strip()]

    def set_name(self, name: str):
        """Set the pharmacy name"""
        name_input = self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT))
        name_input.clear()
        name_input.send_keys(name)

    def set_address(self, address: str):
        """Set the pharmacy address"""
        address_input = self.wait.until(EC.visibility_of_element_located(self.ADDRESS_INPUT))
        address_input.clear()
        address_input.send_keys(address)

    def set_postal_code(self, postal_code: str):
        """Set the postal code"""
        postal_code_input = self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE_INPUT))
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)

    def select_group(self, group_name: str):
        """Select pharmacy group from the dropdown"""
        group_input = self.wait.until(EC.element_to_be_clickable(self.GROUP_SELECT))
        group_input.click()
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{group_name}')]")))
        option.click()

    def save(self):
        """Click Save button"""
        save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_button.click()

    def select_group(self, group_name: str):
        group_input = self.wait.until(EC.element_to_be_clickable(self.GROUP_SELECT))
        group_input.click()
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{group_name}')]")))
        option.click()

    def select_default_label_printer(self, printer_name: str):
        self._select_dropdown_option(self.LABEL_PRINTER_SELECT, printer_name)

    def select_default_a4_printer(self, printer_name: str):
        self._select_dropdown_option(self.A4_PRINTER_SELECT, printer_name)

    def select_default_receipt_printer(self, printer_name: str):
        self._select_dropdown_option(self.RECEIPT_PRINTER_SELECT, printer_name)

    def _select_dropdown_option(self, locator, text: str):
        dropdown = self.wait.until(EC.element_to_be_clickable(locator))
        dropdown.click()
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{text}')]")))
        option.click()

    def save(self):
        save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_button.click()

    def should_see_notification(self, expected_text: str = "Pharmacy was created"):
        notification = self.wait.until(EC.visibility_of_element_located(self.NOTIFICATION))
        assert expected_text in notification.text, f"Expected '{expected_text}', got '{notification.text}'"

    def create_pharmacy(self, name: str, data: dict = pharmacy_data):
        """Заполняет форму создания аптеки и сохраняет"""
        self.clear_and_type(self.driver.find_element(*self.NAME_INPUT), name)
        self.clear_and_type(self.driver.find_element(*self.ADDRESS_LINE1_INPUT), data["address_line1"])
        self.clear_and_type(self.driver.find_element(*self.ADDRESS_LINE2_INPUT), data["address_line2"])
        self.clear_and_type(self.driver.find_element(*self.TOWN_INPUT), data["town"])
        self.select_from_dropdown("addressCounty", "Dublin")
        self.clear_and_type(self.driver.find_element(*self.EIRCODE_INPUT), data["eircode"])
        self.clear_and_type(self.driver.find_element(*self.GMS_INPUT), data["gms"])
        self.clear_and_type(self.driver.find_element(*self.VAT_INPUT), data["vat_number"])
        self.fill_random_qty_fields()

        self.driver.find_element(*self.SAVE_BUTTON).click()

    def clear_and_type(self, element, value: str):
        """Очистить поле ввода и ввести новое значение"""
        element.click()  # Активировать фокус
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(value)

    def fill_random_qty_fields(self):
        """Заполнить все поля с суффиксом 'Qty' случайными значениями 0 или 1."""
        qty_inputs = self.driver.find_elements(By.XPATH, "//label[contains(text(), 'Qty')]/following-sibling::input")
        for input_element in qty_inputs:
            value = str(random.randint(0, 1))
            self.clear_and_type(input_element, value)

    def open_pharmacy(self, name: str = "Alfa Pharmacy 1"):
        """
        Найти и кликнуть по Аптеке с заданным названием
        """
        group_locator = (By.XPATH, "//div[starts-with(@id, 'pharmacyName_')]")
        elements = self.wait.until(EC.presence_of_all_elements_located(group_locator))

        for el in elements:
            try:
                text = el.find_element(By.XPATH, ".//div").text.strip()
                if text == name:
                    el.click()
                    return
            except Exception:
                continue

        raise AssertionError(f"Pharmacy '{name}' not found on the page.")

    def select_from_dropdown(self, input_id: str, option_text: str, timeout: int = 10):
        wait = WebDriverWait(self.driver, timeout)

        # 1. Находим обёртку v-select по ID input-поля
        field_wrapper_xpath = f'//input[@id="{input_id}"]/ancestor::div[contains(@class, "v-select")]'
        field_wrapper = wait.until(EC.presence_of_element_located((By.XPATH, field_wrapper_xpath)))

        # 2. Скроллим и кликаем по выпадающему списку (по обёртке)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", field_wrapper)
        ActionChains(self.driver).move_to_element(field_wrapper).pause(0.3).click().perform()

        # 3. Подождать появления dropdown-меню
        # Vuetify вставляет меню в конец body как <ul role="listbox"> или <div role="listbox">
        option_xpath = f'//div[@role="listbox"]//div[contains(@class, "v-list-item-title") and normalize-space(text())="{option_text}"]'

        try:
            option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
            option.click()
        except Exception as e:
            # debug fallback: выводим весь body если не найден элемент
            print("Dropdown option not found or not clickable. Trying fallback click.")
            print(self.driver.page_source)
            raise e

    def edit_pharmacy(self, new_name: str):
        """Edit only the pharmacy name and save changes"""
        name_input = self.wait.until(EC.visibility_of_element_located((By.ID, "nameTextField")))
        self.clear_and_type(name_input, new_name)

        # Нажать кнопку Save
        save_button = self.wait.until(EC.element_to_be_clickable((By.ID, "saveButton")))
        save_button.click()

        # Подтвердить, что имя сохранено (можно использовать wait для оповещения или загрузки)
        self.wait.until(EC.text_to_be_present_in_element_value((By.ID, "nameTextField"), new_name))

    def open_ordering_tab(self, tab_name: str):
        """
        Click the ordering tab with the given name (e.g., "Suppliers", "Wholesalers", etc.)
        """
        # XPath находит кнопку с нужным текстом внутри .v-btn
        xpath = f"//button[contains(@class, 'v-btn') and .//div[contains(text(), '{tab_name}')]]"
        tab_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        tab_button.click()

    def select_supplier_from_dropdown(self, supplier_name: str):
        # 1. Клик по input (через JS для обхода overlay)
        self.driver.execute_script("document.getElementById('supplierIntegrationDialogSupplierName').click();")

        # 2. Ввод текста
        input_field = self.wait.until(EC.element_to_be_clickable((By.ID, "supplierIntegrationDialogSupplierName")))
        input_field.clear()
        input_field.send_keys(supplier_name)

        # # 3. Подождать появления выпадающего меню
        option_xpath = f"//div[@role='option']//span[contains(text(), '{supplier_name}')]"
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option.click()

    def add_supplier_integration(self, supplier_name: str):
        """Add a supplier integration with default test data"""
        self.wait.until(EC.element_to_be_clickable(self.ADD_SUPPLIER_BUTTON)).click()

        # Выбор поставщика из дропдауна

        self.select_supplier_from_dropdown(supplier_name)

        # Ввод остальных данных
        supplier_info_label = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[contains(@class, 'text-subtitle-1') and text()='Supplier Info']"
        )))
        supplier_info_label.click()
        toggle_label = self.wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "label[for='supplierIntegrationDialogIntegrationSwitch']"
        )))
        toggle_label.click()

        self.js_click_and_type(self.PHONE_INPUT, "123456789"),
        self.js_click_and_type(self.EMAIL_INPUT, "123456789"),
        self.js_click_and_type(self.ACCOUNT_INPUT, "1234567")
        self.js_click_and_type(self.PASSWORD_INPUT, "password")

        # Сохранить
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON_INTEGRATION)).click()

    def should_see_enabled_integration(self, supplier_name: str):
        """
        Проверить, что у поставщика указан статус Enabled.
        """
        xpath = f"//tr[contains(@class, 'v-data-table__tr')]//td[div[contains(text(), '{supplier_name}')]]/following-sibling::td//div[contains(text(), 'Enabled')]"
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        assert "Enabled" in element.text, f"Expected supplier '{supplier_name}' to be enabled, but got '{element.text}'"
        time.sleep(1)

    def delete_supplier_integration(self, supplier_name: str):
        """
        Удалить интеграцию указанного поставщика.
        """
        # Находим строку с нужным поставщиком
        row_xpath = f"//tr[contains(@class, 'v-data-table__tr')]//td[div[contains(text(), '{supplier_name}')]]/parent::tr"
        row = self.wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

        # Внутри строки ищем кнопку удаления
        delete_button = row.find_element(By.XPATH, ".//button[starts-with(@id, 'removeSupplierIntegrationButton_3')]")
        delete_button.click()

    def js_click_and_type(self, by_locator: tuple, value: str):
        """
        Кликает по элементу через JavaScript и вводит значение.
        :param by_locator: кортеж локатора (By.ID, "some_id")
        :param value: значение для ввода
        """
        element = self.driver.find_element(*by_locator)
        self.driver.execute_script("arguments[0].click();", element)
        self.clear_and_type(element, value)

    def fill_contact_details(self, phone_1: str, phone_2: str, email_1: str, email_2: str):
        """Add a supplier integration with default test data"""
        time.sleep(1)
        self.js_click_and_type(self.CONTACT_PHONE_1, phone_1)
        self.js_click_and_type(self.CONTACT_PHONE_2, phone_2),
        self.js_click_and_type(self.CONTACT_EMAIL_1, email_1)
        self.js_click_and_type(self.CONTACT_EMAIL_2, email_2)
        # Сохранить
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()


    def should_see_saved_contact_details(self, email_1: str, email_2: str, phone_1: str, phone_2: str):
        """Проверка, что контактные данные были сохранены корректно"""
        phone_1_value = self.driver.find_element(*self.CONTACT_PHONE_1).get_attribute("value")
        phone_2_value = self.driver.find_element(*self.CONTACT_PHONE_2).get_attribute("value")
        email_1_value = self.driver.find_element(*self.CONTACT_EMAIL_1).get_attribute("value")
        email_2_value = self.driver.find_element(*self.CONTACT_EMAIL_2).get_attribute("value")

        assert phone_1_value == phone_1, f"Expected phone 1 to be '{phone_1}', but got '{phone_1_value}'"
        assert phone_2_value == phone_2, f"Expected phone 2 to be '{phone_2}', but got '{phone_2_value}'"
        assert email_1_value == email_1, f"Expected email 1 to be '{email_1}', but got '{email_1_value}'"
        assert email_2_value == email_2, f"Expected email 2 to be '{email_2}', but got '{email_2_value}'"

    def should_see_contact_validation_errors(self):
        """Проверка, что отображаются ошибки валидации в контактных полях"""

        errors = {
            "phone1TextField-messages": "Phone is not valid",
            "phone2TextField-messages": "Phone is not valid",
            "email1TextField-messages": "Email is not valid",
            "email2TextField-messages": "Email is not valid"
        }

        for message_id, expected_text in errors.items():
            error_element = self.wait.until(EC.visibility_of_element_located((By.ID, message_id)))
            actual_text = error_element.text.strip()
            assert expected_text in actual_text, (
                f"Expected validation message '{expected_text}' in '{message_id}', but got '{actual_text}'"
            )

    def add_employee(self, email: str):
        """Добавляет сотрудника по email"""
        # 1. Нажимаем кнопку "Add Employee"
        add_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "addEmployeeButton")))
        add_btn.click()

        # 2. Ждём появления строки с нужным email
        row_xpath = f"//tr[contains(@class, 'v-data-table__tr')]//td[contains(text(), '{email}')]"
        row = self.wait.until(EC.element_to_be_clickable((By.XPATH, row_xpath)))
        row.click()

        # 3. Нажимаем "Save"
        save_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "saveButton")))
        save_btn.click()
        self.should_see_success_message(expected="Pharmacy was updated")

    def should_see_success_message(self, expected: str = "Organisation was updated"):
        message = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        assert expected in message.text, f"Expected message '{expected}', but got '{message.text}'"

    def should_see_employee(self, email: str):
        """Проверяет, что сотрудник с указанным email отображается в таблице"""
        employee_row_xpath = f"//tr[contains(@class, 'v-data-table__tr')]//td[contains(text(), '{email}')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, employee_row_xpath)),
                        message=f"Сотрудник с email '{email}' не найден в списке")


    def delete_employee(self, email: str):
        """Удаляет сотрудника с указанным email"""
        # Найти строку сотрудника по email
        row_xpath = f"//tr[contains(@class, 'v-data-table__tr')]//td[contains(text(), '{email}')]/parent::tr"
        employee_row = self.wait.until(EC.visibility_of_element_located((By.XPATH, row_xpath)))

        # Найти кнопку удаления внутри этой строки
        delete_button = employee_row.find_element(By.XPATH, ".//button[starts-with(@id, 'removeEmployeeButton')]")

        # Клик по кнопке удаления
        delete_button.click()
