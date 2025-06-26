import pytest
import allure

from pages.base_page import BasePage
from pages.pharmacy_group_page import PharmacyGroupPage


@allure.suite("Management tests")
@allure.feature("Pharmacy groups")
@allure.title("User can't Delete Default pharmacy group")
def test_cannot_delete_default_group(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.open_group(name="sarah test group")
    page.should_not_see_delete_button()
    page.should_not_see_delete_icon_near_pharmacies()


@allure.title("Change default group")
def test_change_default_pharmacy_group(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.open_group(name="Alfa Pharmacy Group First")
    page.mark_as_default()
    page.save_changes()
    page.should_see_notification_message()
    page.should_see_default_group_label()
    base.open("pharmacyGroups")
    page.open_group(name="sarah test group")
    page.mark_as_default()
    page.save_changes()
    page.should_see_notification_message()


@allure.title("Delete pharmacy group")
def test_delete_pharmacy_group(driver):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.navigate_to_groups()
    page.open()
    page.delete_group()
    page.should_be_deleted()


@allure.title("Group becomes default after deleting current group")
def test_group_becomes_default_after_deletion(driver):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.open()
    page.add_pharmacy("Pharmacy 1")
    page.delete_group(confirm=True)
    page.should_be_default_group("Pharmacy 1")


@allure.title("Search for pharmacy group")
def test_search_pharmacy_group(driver):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.open_section()
    page.search("Group A")
    page.should_show_result("Group A")
    page.select_result("Group A")
    page.should_open_group("Group A")


@allure.title("Create pharmacy group")
def test_create_pharmacy_group(driver):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.open()
    page.create_group("New Group", pharmacies=["Pharmacy A", "Pharmacy B"])
    page.should_see_group("New Group")


@allure.title("Change Pharmacy Group for pharmacy")
def test_change_group_for_pharmacy(driver):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.open()
    page.add_pharmacy_from_other_group("Pharmacy X")
    page.confirm_change_group()
    page.should_show_group_updated_message()


@allure.title("Group becomes default after removing last pharmacy")
def test_group_becomes_default_after_removing_last_pharmacy(driver):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.open()
    page.add_pharmacy("Pharmacy 1")
    page.delete_pharmacy("Pharmacy 1")
    page.save_changes()
    page.should_be_default_group("Pharmacy 1")


@allure.title("Delete pharmacy from group")
def test_delete_pharmacy_from_group(driver):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.delete_pharmacy("Pharmacy Y")
    page.go_back()
    page.open_again()
    page.should_see_group_empty()


@allure.title("Edit pharmacy group")
def test_edit_pharmacy_group(driver):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.delete_pharmacy("Old Pharmacy")
    page.add_pharmacy("Pharmacy A")
    page.add_pharmacy("Pharmacy B")
    page.go_back()
    page.open_again()
    page.should_see_pharmacies(["Pharmacy A", "Pharmacy B"])


@allure.title("Create default pharmacy group and link pharmacy")
def test_create_default_pharmacy_group(driver):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.set_as_default()
    page.go_to_pharmacies()
    page.create_pharmacy("New Pharmacy")
    page.search("New Pharmacy")
    page.should_see_pharmacy("New Pharmacy")
