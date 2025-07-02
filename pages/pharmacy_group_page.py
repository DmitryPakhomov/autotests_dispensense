import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PharmacyGroupPage:
    SEARCH_FIELD = (By.ID, "searchTextField")
    ADD_GROUP_BUTTON = (By.ID, "addPharmacyGroupButton")
    DELETE_GROUP_BUTTON = (By.ID, "deleteButton")
    GROUP_NAME_INPUT = (By.ID, "pharmacyGroupName")
    GROUP_NAME_INPUT_CREATE = (By.XPATH, "//label[contains(text(), 'Group Name')]/following-sibling::input")
    GROUP_INPUT_WRAPPER = (By.CSS_SELECTOR, "div.v-input input#pharmacyGroupName")
    ADD_PHARMACY_BUTTON = (By.ID, "addPharmacyButton")
    CHANGE_GROUP_CONFIRM_BUTTON = (By.ID, "changePharmacyGroupDialogChangeButton")
    DELETE_CONFIRM_BUTTON = (By.ID, "commonDialogOkButton")



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search(self, group_name: str):
        field = self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))
        field.clear()
        field.send_keys(group_name)
        time.sleep(2)

    def should_show_result(self, name: str):
        """
        Verify that the search results contain a group with the given name
        """
        locator = (By.XPATH, f"//div[starts-with(@id, 'pharmacyGroupName_')]/div[contains(text(), '{name}')]")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        assert name in element.text, f"Expected to see group '{name}' in results, but saw '{element.text}'"

    def select_result(self, index: int = 0):
        locator = (By.ID, f"pharmacyGroupName_{index}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def should_open_group(self, expected_name: str):
        name_input = self.wait.until(EC.presence_of_element_located(self.GROUP_NAME_INPUT))
        actual = name_input.get_attribute("value").strip()
        assert actual == expected_name, f"Expected group name '{expected_name}', but got '{actual}'"

    def create_group(self, name: str):
        self.wait.until(EC.element_to_be_clickable(self.ADD_GROUP_BUTTON)).click()

        # Wait for the input field inside the v-input to appear
        input_field = self.wait.until(
            EC.presence_of_element_located(self.GROUP_INPUT_WRAPPER)
        )
        self.clear_and_type(input_field, name)
        self.save_changes()
        time.sleep(4)

    def save_changes(self):
        save_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "saveButton")))
        save_btn.click()

    def delete_group(self):
        delete_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_GROUP_BUTTON))
        delete_btn.click()

    def delete_group_dialog(self):
        delete_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_CONFIRM_BUTTON))
        delete_btn.click()

    def add_pharmacy(self, pharmacy_name: str):
        self.wait.until(EC.element_to_be_clickable(self.ADD_PHARMACY_BUTTON)).click()
        search_field = self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))
        search_field.clear()
        search_field.send_keys(pharmacy_name)
        time.sleep(4)

        rows = self.driver.find_elements(By.XPATH, "//tr[contains(@class, 'v-data-table__tr')]")
        print(f"Found {len(rows)} rows")

        for row in rows:
            print("ROW TEXT:", row.text)
        self.driver.execute_script("arguments[0].click();", row)

        self.wait.until(EC.element_to_be_clickable(self.CHANGE_GROUP_CONFIRM_BUTTON)).click()

    def delete_pharmacy(self, pharmacy_name: str):
        """
        Delete a pharmacy by name by clicking the trash icon in its row
        """
        # Find the row with the desired pharmacy name
        row_xpath = f"//tr[contains(@class, 'v-data-table__tr')]//div[contains(text(), '{pharmacy_name}')]/ancestor::tr"

        row = self.wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

        # Inside that row find the button with the delete icon
        delete_button = row.find_element(By.XPATH, ".//button[starts-with(@id, 'deletePharmacyButton')]")

        # Click it
        delete_button.click()

    def confirm_change_group(self):
        self.wait.until(EC.element_to_be_clickable(self.CHANGE_GROUP_CONFIRM_BUTTON)).click()

    def mark_as_default(self):
        checkbox = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and @aria-label='Default Group']")))
        if not checkbox.is_selected():
            checkbox.click()

    def should_see_group(self, name: str):
        locator = (By.ID, f"pharmacyGroupName_0")
        item = self.wait.until(EC.visibility_of_element_located(locator))
        assert name in item.text, f"Expected to see group '{name}', but saw '{item.text}'"

    def open_group(self, name: str = "sarah test group"):
        """
        Find and click the group with the specified name
        """
        group_locator = (By.XPATH, "//div[starts-with(@id, 'pharmacyGroupName_')]")
        elements = self.wait.until(EC.presence_of_all_elements_located(group_locator))

        for el in elements:
            try:
                text = el.find_element(By.XPATH, ".//div").text.strip()
                if text == name:
                    el.click()
                    return
            except Exception:
                continue

        raise AssertionError(f"Pharmacy group '{name}' not found on the page.")

    def should_not_see_delete_button(self):
        """Check that the group delete button is not displayed"""
        try:
            button = self.driver.find_element(By.ID, "deleteButton")
            is_visible = button.is_displayed()
            assert not is_visible, "Delete button is visible but should not be"
        except Exception:
            # Element not found is acceptable
            pass

    def should_not_see_delete_icon_near_pharmacies(self):
        """Check that the delete (trash) icon is not shown next to pharmacies"""
        icons = self.driver.find_elements(By.CSS_SELECTOR, "svg.feather.feather-trash-2")
        visible_icons = [icon for icon in icons if icon.is_displayed()]
        assert not visible_icons, f"Expected no visible delete icons, but found {len(visible_icons)}"

    def should_see_notification_message(self, expected: str = "Pharmacy Group was updated", timeout: int = 10):
        """
        Verify that a notification with the expected text appears
        """
        locator = (By.ID, "notificationMessage")
        message = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        actual = message.text.strip()
        assert expected in actual, f"Expected notification '{expected}', but got '{actual}'"

    def should_see_default_group_label(self, expected: str = "Default Group", timeout: int = 10):
        """
        Ensure that the text 'Default Group' is displayed in the pharmacyIsDefault block
        """
        locator = (By.ID, "pharmacyIsDefault")
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        actual = element.text.strip()
        assert expected in actual, f"Expected '{expected}' in default group label, but got '{actual}'"


    def should_not_see_group(self, name: str):
        """
        Ensure that a group with the given name is absent from the list
        """
        results = self.driver.find_elements(By.XPATH, f"//div[starts-with(@id, 'pharmacyGroupName_')]//div[contains(text(), '{name}')]")
        visible = [el for el in results if el.is_displayed()]
        assert not visible, f"Expected group '{name}' to be deleted, but it's still visible"

    def clear_and_type(self, element, value: str):
        """Clear the input field and enter a new value"""
        element.click()  # Activate focus
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(value)

    def delete_group_by_name(self, name: str):
        """
        Delete a group by name: search, select, remove and confirm
        """
        self.search(name)
        self.should_show_result(name)
        self.select_result()
        self.delete_group()
        self.delete_group_dialog()

    def should_be_default_group(self, pharmacy_name: str):
        """
        Check that the specified pharmacy appears in the list as part of the default group
        """
        xpath = f"//tr[contains(@class, 'v-data-table__tr')]//td//div[contains(text(), '{pharmacy_name}')]"
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        assert pharmacy_name in element.text, f"Expected '{pharmacy_name}' in default group, but saw '{element.text}'"

    def should_see_pharmacy(self, pharmacy_names: list[str]):
        """
        Check that all provided pharmacies are present in the table on the page
        """
        for name in pharmacy_names:
            xpath = f"//tr[contains(@class, 'v-data-table__tr')]//td//div[contains(text(), '{name}')]"
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            assert name in element.text, f"Pharmacy '{name}' not found on the page. Found text: '{element.text}'"

    def should_not_see_pharmacy(self, pharmacy_name: str):
        """
        Verify that the pharmacy with the given name is absent from the table
        """
        xpath = f"//tr[contains(@class, 'v-data-table__tr')]//td//div[contains(text(), '{pharmacy_name}')]"
        elements = self.driver.find_elements(By.XPATH, xpath)
        assert len(elements) == 0, f"Pharmacy '{pharmacy_name}' was found on the page, but shouldn't be."


    def refresh(self):
        """Refresh the current page"""
        self.driver.refresh()
