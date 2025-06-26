import pytest
import allure
from pages.tenant_page import TenantPage
from pages.base_page import BasePage


@allure.suite("Management tests")
@allure.feature("Tenant")
@allure.title("Edit tenant name and description")
def test_edit_tenant_info(login):
    base = BasePage(login.driver)
    base.open("tenants")

    page = TenantPage(login.driver)
    page.set_name("Updated Org Name")
    page.set_description("New description for the organization")
    page.save_changes()
    page.should_see_success_message("Successfully updated")

    page.should_have_name("Updated Org Name")
    page.should_have_description("New description for the organization")


# @allure.title("Validation: name is required")
# def test_tenant_name_required(login):
#     page = TenantPage(login.driver)
#     page.open()
#     page.set_name("")  # Очистим поле
#     page.save_changes()
#     page.should_see_field_error("name", "Name is required")
#
#
# @allure.title("Get current tenant info")
# def test_read_tenant_info(login):
#     page = TenantPage(login.driver)
#     page.open()
#     name, description = page.get_tenant_info()
#     assert isinstance(name, str) and name != ""
#     assert isinstance(description, str)
