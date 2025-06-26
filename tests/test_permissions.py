import pytest
import allure
from pages.employee_page import EmployeePage
from pages.role_page import RolePage
from pages.workstation_page import WorkstationPage
from pages.pharmacy_group_page import PharmacyGroupPage


@allure.suite("Management tests")
@allure.feature("Management actions")
@allure.title("Manage roles")
def test_manage_roles(driver):
    page = RolePage(driver)
    page.open()
    page.create_role("Test Role")
    page.should_see_role("Test Role")
    page.delete_role("Test Role")
    page.should_not_see_role("Test Role")


@allure.title("Manage workstations without ReadWorkstationList action")
def test_manage_workstations_without_permission(driver):
    page = WorkstationPage(driver)
    page.logout()
    page.should_not_see_workstation_button()


@allure.title("Manage pharmacy group without ReadPharmacyGroupList action")
def test_manage_pharmacy_group_without_permission(driver):
    page = PharmacyGroupPage(driver)
    page.logout()
    page.should_not_see_pharmacy_group_button()


@allure.title("Manage roles without ReadRole action")
def test_manage_roles_without_permission(driver):
    page = RolePage(driver)
    page.logout()
    page.should_not_see_role_button()
