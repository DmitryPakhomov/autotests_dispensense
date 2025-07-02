from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By


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
        "gms": "123456",
        "vat_number": "VAT123456",
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
        """Verify that a pharmacy with the specified name appears in the list"""
        xpath = f"//tr[contains(@class, 'v-data-table__tr')]//div[contains(text(), '{name}')]"
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        assert name in element.text, f"Expected to see pharmacy '{name}', but got '{element.text}'"

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
        self.clear_and_type(self.driver.find_element(*self.NAVI_ACCOUNT_INPUT), data["navi_account"])
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
        """
        Открыть dropdown по input_id и выбрать нужное значение по тексту.

        :param input_id: id поля <input>, связанного с селектом (например 'addressCounty')
        :param option_text: текст опции, которую нужно выбрать
        """
        # Найти инпут по id
        input_el = self.driver.find_element(By.ID, input_id)

        # Нажать на поле, чтобы открыть список
        input_el.click()

        # Подождать появления нужной опции
        option_xpath = f"//div[@role='listbox']//div[contains(@class, 'v-list-item-title') and normalize-space(text())='{option_text}']"
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, option_xpath))
        )

        # Нажать на опцию
        self.driver.find_element(By.XPATH, option_xpath).click()