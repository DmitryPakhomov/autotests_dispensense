import pytest
import allure
from pages.device_page import DevicePage


@allure.suite("Management tests")
@allure.feature("Devices")
@allure.title("Add label printer")
def test_add_label_printer(driver):
    page = DevicePage(driver)
    page.open()
    page.add_device("New Label Printer")
    page.should_see_device("New Label Printer")


@allure.title("Add image scanner")
def test_add_image_scanner(driver):
    page = DevicePage(driver)
    page.open()
    page.add_device("New Image Scanner")
    page.should_see_device("New Image Scanner")


@allure.title("Add matrix printer")
def test_add_matrix_printer(driver):
    page = DevicePage(driver)
    page.open()
    page.add_device("New Matrix Printer")
    page.should_see_device("New Matrix Printer")


@allure.title("Add folder scanner")
def test_add_folder_scanner(driver):
    page = DevicePage(driver)
    page.open()
    page.add_device("New Folder Scanner")
    page.should_see_device("New Folder Scanner")


@allure.title("Edit folder scanner")
def test_edit_folder_scanner(driver):
    page = DevicePage(driver)
    page.open()
    page.edit_device("New Folder Scanner", "Edited Folder Scanner")
    page.should_see_device("Edited Folder Scanner")


@allure.title("Edit label printer")
def test_edit_label_printer(driver):
    page = DevicePage(driver)
    page.open()
    page.edit_device("New Label Printer", "Edited Label Printer")
    page.should_see_device("Edited Label Printer")


@allure.title("Edit matrix printer")
def test_edit_matrix_printer(driver):
    page = DevicePage(driver)
    page.open()
    page.edit_device("New Matrix Printer", "Edited Matrix Printer")
    page.should_see_device("Edited Matrix Printer")


@allure.title("Filter devices")
def test_filter_devices(driver):
    page = DevicePage(driver)
    page.open()
    page.apply_filter("Scanner")
    page.should_see_filtered_results("Scanner")


@allure.title("Device dialog validations")
def test_device_dialog_validations(driver):
    page = DevicePage(driver)
    page.open()
    page.open_add_device_dialog()
    page.save_without_required_fields()
    page.should_see_validation_errors()


@allure.title("Manage devices without ReadDeviceList action")
def test_manage_devices_without_permission(driver):
    page = DevicePage(driver)
    page.logout()
    page.should_see_devices_button()
