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
    base.open("pharmacies")
    page.open_pharmacy(name)
    time.sleep(1)
    page.should_see_pharmacy(name)


@allure.title("Edit pharmacy")
def test_edit_pharmacy(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.click_add_pharmacy()
    name = f"Test Pharmacy {int(time.time())}"
    page.create_pharmacy(name)
    base.open("pharmacies")
    page.open_pharmacy(name)
    new_name = f"Test Pharmacy {int(time.time())}"
    page.edit_pharmacy(new_name)
    page.should_see_pharmacy(new_name)


# @allure.title("Add pharmacy integration")  #TODO решили не делать
# def test_add_pharmacy_integration(driver, login):
#     base = BasePage(login.driver)
#     base.open("pharmacies")
#
#     page = PharmacyPage(driver, login)
#     page.open_pharmacy("Updated Pharmacy")
#     page.open_integrations_tab()
#     page.add_integration("Integration X")
#     page.should_see_integration("Integration X")


# @allure.title("Edit pharmacy integration") #TODO решили не делать
# def test_edit_pharmacy_integration(driver, login):
#     base = BasePage(login.driver)
#     base.open("pharmacies")
#
#     page = PharmacyPage(driver)
#     page.open_pharmacy("Updated Pharmacy")
#     page.open_integrations_tab()
#     page.edit_integration("Integration X", "Integration Y")
#     page.should_see_integration("Integration Y")



@allure.title("Enable supplier integration")
def test_enable_supplier_integration(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")

    page = PharmacyPage(driver)
    page.open_pharmacy("Alfa Pharmacy 1")
    page.open_ordering_tab("Suppliers")
    page.add_supplier_integration("Bonus")
    page.should_see_enabled_integration("Bonus")
    page.delete_supplier_integration("Bonus")

@allure.title("Add valid pharmacy contact details")
def test_valid_pharmacy_contact(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")
    email_1 = "info@pharmacy.com"
    email_2 = "info2@pharmacy.com"
    phone_1 = "123456229"
    phone_2 = "123456789"
    name = f"Test Pharmacy {int(time.time())}"
    page = PharmacyPage(driver)
    page.click_add_pharmacy()
    page.create_pharmacy(name)
    base.open("pharmacies")
    page.open_pharmacy(name)
    page.open_ordering_tab("Contact Details")
    page.fill_contact_details(
        phone_1=phone_1,
        phone_2=phone_2,
        email_1=email_1,
        email_2=email_2
    )
    page.should_see_saved_contact_details(
        phone_1=phone_1,
        phone_2=phone_2,
        email_1=email_1,
        email_2=email_2
    )

@allure.title("Add invalid pharmacy contact details")
def test_invalid_pharmacy_contact(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")
    email_1 = "info"
    email_2 = "info2"
    phone_1 = " "
    phone_2 = " "
    name = f"Test Pharmacy {int(time.time())}"
    page = PharmacyPage(driver)
    page.click_add_pharmacy()
    page.create_pharmacy(name)
    base.open("pharmacies")
    page.open_pharmacy(name)
    page.open_ordering_tab("Contact Details")
    page.fill_contact_details(
        phone_1=phone_1,
        phone_2=phone_2,
        email_1=email_1,
        email_2=email_2
    )
    page.should_see_contact_validation_errors()

@allure.title("Add employee to pharmacy")
def test_add_employee_to_pharmacy(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")
    employee = "234234@gmail.com"
    name = f"Test Pharmacy {int(time.time())}"
    page = PharmacyPage(driver)
    page.click_add_pharmacy()
    page.create_pharmacy(name)
    base.open("pharmacies")
    page.open_pharmacy(name)
    page.open_ordering_tab("Employees")
    page.add_employee(employee)
    page.should_see_employee(employee)


@allure.title("Add employee to pharmacy")
def test_add_employee_and_delete_to_pharmacy(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacies")
    employee = "234234@gmail.com"
    name = f"Test Pharmacy {int(time.time())}"
    page = PharmacyPage(driver)
    page.click_add_pharmacy()
    page.create_pharmacy(name)
    base.open("pharmacies")
    page.open_pharmacy(name)
    page.open_ordering_tab("Employees")
    page.add_employee(employee)
    page.should_see_employee(employee)
    page.delete_employee(employee)
    page.should_not_see_employee(employee)
