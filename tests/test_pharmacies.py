import time
import pytest
import allure

from pages.base_page import BasePage
from pages.pharmacy_page import PharmacyPage


@allure.suite("Management tests")
@allure.feature("Pharmacies")
@allure.title("Create pharmacy")
def test_create_pharmacy(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.click_add_pharmacy()
    name = f"Test Pharmacy {int(time.time())}"
    page.create_pharmacy(name)
    page.open_pharmacy(name)
    page.should_see_pharmacy(name)


@allure.title("Edit pharmacy")
def test_edit_pharmacy(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    old_name = "Test Pharmacy"
    new_name = f"Updated Pharmacy {int(time.time())}"
    page.open_pharmacy(old_name)
    page.edit_pharmacy(old_name, new_name)
    page.open_pharmacy(new_name)
    page.should_see_pharmacy(new_name)


@allure.title("Add pharmacy integration")
def test_add_pharmacy_integration(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver, login)
    page.open_pharmacy("Updated Pharmacy")
    page.open_integrations_tab()
    page.add_integration("Integration X")
    page.should_see_integration("Integration X")


@allure.title("Edit pharmacy integration")
def test_edit_pharmacy_integration(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.open_pharmacy("Updated Pharmacy")
    page.open_integrations_tab()
    page.edit_integration("Integration X", "Integration Y")
    page.should_see_integration("Integration Y")


@allure.title("Remove supplier integration")
def test_remove_supplier_integration(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.open_pharmacy("Updated Pharmacy")
    page.open_ordering_tab()
    page.add_supplier_integration("Test Supplier")
    page.remove_supplier_integration("Test Supplier")
    page.should_see_ordering_tab_empty()


@allure.title("Enable supplier integration")
def test_enable_supplier_integration(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.open_pharmacy("Updated Pharmacy")
    page.open_ordering_tab()
    page.add_supplier_integration("Supplier A")
    page.enable_integration("Supplier A")
    page.should_see_enabled_integration("Supplier A")


@allure.title("Add invalid pharmacy contact details")
def test_invalid_pharmacy_contact(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.open_pharmacy("Updated Pharmacy")
    page.open_contact_tab()
    page.fill_invalid_contact_details()
    page.should_see_contact_validation_errors()


@allure.title("Add valid pharmacy contact details")
def test_valid_pharmacy_contact(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.open_pharmacy("Updated Pharmacy")
    page.open_contact_tab()
    page.fill_contact_details(email="info@pharmacy.com", phone="+123456789")
    page.should_see_saved_contact_details()


@allure.title("Add employee to pharmacy")
def test_add_employee_to_pharmacy(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.open_pharmacy("Updated Pharmacy")
    page.open_employees_tab()
    page.add_employee("John Smith", role="Pharmacist")
    page.should_see_employee("John Smith")


@allure.title("Delete employee from pharmacy")
def test_delete_employee_from_pharmacy(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.open_pharmacy("Updated Pharmacy")
    page.open_employees_tab()
    page.delete_employee("John Smith")
    page.should_see_employees_tab_empty()


@allure.title("Read pharmacy without ReadPharmacyList action")
def test_read_pharmacy_without_permission(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.logout()
    page.should_see_pharmacy_button_in_menu()
