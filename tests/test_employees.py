import pytest
import allure
from pages.employee_page import EmployeePage


@allure.suite("Management tests")
@allure.feature("Employees")
@allure.title("Add employee")
def test_add_employee(driver):
    page = EmployeePage(driver)
    page.open()
    page.create_employee("Pharmacist", "Pharmacy A")
    page.search_employee("John Smith")
    page.should_see_employee("John Smith")


@allure.title("Edit employee")
def test_edit_employee(driver):
    page = EmployeePage(driver)
    page.search_employee("John Smith")
    page.edit_employee("John Smith", "Technician")
    page.should_see_employee_with_role("John Smith", "Technician")


@allure.title("Delete and restore employee")
def test_delete_and_restore_employee(driver):
    page = EmployeePage(driver)
    page.search_employee("John Smith")
    page.delete_employee("John Smith")
    page.filter_deleted()
    page.restore_employee("John Smith")
    page.reset_filter()
    page.should_see_employee("John Smith")


@allure.title("Reinvite employee")
def test_reinvite_employee(driver):
    page = EmployeePage(driver)
    page.search_employee("John Smith")
    page.reinvite_employee("John Smith")
    page.should_see_reinvite_success("John Smith")


@allure.title("Try to open Employees page without rights")
def test_open_employees_page_without_rights(driver):
    page = EmployeePage(driver)
    page.logout()
    page.should_see_employees_button()


@allure.title("Try to edit employee without rights")
def test_edit_employee_without_rights(driver):
    page = EmployeePage(driver)
    page.logout()
    page.go_to_employees_page()
    page.should_not_see_edit_button("John Smith")


@allure.title("Try to delete employee without rights")
def test_delete_employee_without_rights(driver):
    page = EmployeePage(driver)
    page.logout()
    page.go_to_employees_page()
    page.should_not_see_delete_button("John Smith")


@allure.title("Try to create employee without rights")
def test_create_employee_without_rights(driver):
    page = EmployeePage(driver)
    page.logout()
    page.go_to_employees_page()
    page.should_not_see_add_button()


@allure.title("Try to restore employee without RestoreEmployee action")
def test_restore_employee_without_rights(driver):
    page = EmployeePage(driver)
    page.logout()
    page.go_to_deleted_employees()
    page.should_not_see_restore_button("John Smith")
