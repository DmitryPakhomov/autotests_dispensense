# This module contains tests for managing pharmacy groups.
# The scenarios cover creation, deletion and editing of groups.
import time
import pytest
import allure

from pages.base_page import BasePage
from pages.pharmacy_group_page import PharmacyGroupPage


@allure.suite("Management tests")
@allure.feature("Pharmacy groups")
@allure.title("User can't Delete Default pharmacy group")
# Ensure the default group cannot be deleted.
def test_cannot_delete_default_group(driver, login):
    # Open Pharmacy Groups section
    base = BasePage(login.driver)
    base.open("pharmacyGroups")

    page = PharmacyGroupPage(driver)
    page.open_group(name="sarah test group")
    page.should_not_see_delete_button()
    page.should_not_see_delete_icon_near_pharmacies()


@allure.title("Change default group")
# Switch the default pharmacy group and restore the original default.
def test_change_default_pharmacy_group(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")
    page = PharmacyGroupPage(driver)

    # Create and mark a new group as default
    group_name = f"Test Group {int(time.time())}"
    page.create_group(group_name)
    page.mark_as_default()
    page.save_changes()
    page.should_see_notification_message()
    page.should_see_default_group_label()

    # Revert default group to "sarah test group"
    base.open("pharmacyGroups")
    page.open_group(name="sarah test group")
    page.mark_as_default()
    page.save_changes()
    page.should_see_notification_message()

    # Clean up
    base.open("pharmacyGroups")
    page.delete_group_by_name(group_name)


@allure.title("Delete pharmacy group")
# Create a new group and verify it can be deleted.
def test_delete_pharmacy_group(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")
    page = PharmacyGroupPage(driver)

    group_name = f"Test Group {int(time.time())}"
    page.create_group(group_name)
    page.delete_group()
    page.delete_group_dialog()

    # Ensure the group no longer exists
    base.open("pharmacyGroups")
    page.search(group_name)
    page.should_not_see_group(group_name)


@allure.title("Group becomes default after deleting current group")
# After deleting the only pharmacy the group becomes default.
def test_group_becomes_default_after_deletion(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")
    page = PharmacyGroupPage(driver)

    group_name = f"Test Group {int(time.time())}"
    page.create_group(group_name)
    page.add_pharmacy("Alfa Pharmacy 1")
    page.save_changes()
    page.should_see_notification_message()

    page.delete_pharmacy("Alfa Pharmacy 1")
    page.save_changes()
    page.should_see_notification_message()

    # Validate default behavior
    base.open("pharmacyGroups")
    page.open_group("sarah test group")
    page.should_be_default_group("Alfa Pharmacy 1")

    base.open("pharmacyGroups")
    page.delete_group_by_name(group_name)


@allure.title("Search for pharmacy group")
# Search for a pharmacy group and remove the results.
def test_search_pharmacy_group(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")
    page = PharmacyGroupPage(driver)

    group_name_1 = f"Test Group {int(time.time())}"
    group_name_2 = f"Test Group {int(time.time())}"

    page.create_group(group_name_1)
    base.open("pharmacyGroups")
    page.search(group_name_1)
    page.should_show_result(group_name_1)
    page.select_result()
    page.delete_group()
    page.delete_group_dialog()

    page.create_group(group_name_2)
    base.open("pharmacyGroups")
    page.search(group_name_2)
    page.should_show_result(group_name_2)
    page.select_result()
    page.delete_group()
    page.delete_group_dialog()


@allure.title("Create pharmacy group")
# Verify creation of a new pharmacy group.
def test_create_pharmacy_group(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")
    page = PharmacyGroupPage(driver)

    group_name = f"Test Group {int(time.time())}"
    page.create_group(group_name)

    base.open("pharmacyGroups")
    page.search(group_name)
    page.should_see_group(group_name)

    # Clean up
    base.open("pharmacyGroups")
    page.delete_group_by_name(group_name)


@allure.title("Change Pharmacy Group for pharmacy")
# Move a pharmacy from one group to another and verify the change.
def test_change_group_for_pharmacy(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")
    page = PharmacyGroupPage(driver)

    group_name_1 = f"Test Group {int(time.time())}"
    group_name_2 = f"Test Group {int(time.time())}"

    page.create_group(group_name_1)
    page.add_pharmacy("Alfa Pharmacy 1")
    page.save_changes()
    page.should_see_notification_message()

    base.open("pharmacyGroups")
    page.create_group(group_name_2)
    page.add_pharmacy("Alfa Pharmacy 1")
    page.save_changes()
    page.should_see_notification_message()

    # Ensure pharmacy no longer appears in old group
    base.open("pharmacyGroups")
    page.search(group_name_1)
    page.should_show_result(group_name_1)
    page.select_result()
    page.should_not_see_pharmacy("Alfa Pharmacy 1")

    base.open("pharmacyGroups")
    page.delete_group_by_name(group_name_1)
    base.open("pharmacyGroups")
    page.delete_group_by_name(group_name_2)


@allure.title("Delete pharmacy from group")
# Remove a pharmacy from a group and confirm notification.
def test_delete_pharmacy_from_group(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")
    page = PharmacyGroupPage(driver)

    group_name = f"Test Group {int(time.time())}"
    page.create_group(group_name)
    page.add_pharmacy("Alfa Pharmacy 1")
    page.save_changes()
    page.should_see_notification_message()

    page.delete_pharmacy("Alfa Pharmacy 1")
    page.save_changes()
    page.should_see_notification_message()

    base.open("pharmacyGroups")
    page.delete_group_by_name(group_name)


@allure.title("Edit pharmacy group")
# Edit an existing pharmacy group by adding a new pharmacy.
def test_edit_pharmacy_group(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")
    page = PharmacyGroupPage(driver)

    group_name = f"Test Group {int(time.time())}"
    page.create_group(group_name)
    page.add_pharmacy("Alfa Pharmacy 1")
    page.save_changes()
    page.should_see_notification_message()

    page.refresh()
    page.add_pharmacy("Alfa Pharmacy 2")
    page.save_changes()
    page.should_see_notification_message()

    base.open("pharmacyGroups")
    page.search(group_name)
    page.open_group(group_name)
    page.should_see_pharmacy(["Alfa Pharmacy 1", "Alfa Pharmacy 2"])

    base.open("pharmacyGroups")
    page.delete_group_by_name(group_name)


@allure.title("Create default pharmacy group and link pharmacy")
# Create a new default group and link a pharmacy to it.
def test_create_default_pharmacy_group(driver, login):
    base = BasePage(login.driver)
    base.open("pharmacyGroups")
    page = PharmacyGroupPage(driver)

    group_name = f"Test Group {int(time.time())}"
    page.create_group(group_name)
    page.mark_as_default()
    page.save_changes()
    page.should_see_notification_message()
    page.should_see_default_group_label()

    # Revert to default group
    base.open("pharmacyGroups")
    page.open_group("sarah test group")
    page.mark_as_default()
    page.save_changes()
    page.should_see_notification_message()

    base.open("pharmacyGroups")
    page.delete_group_by_name(group_name)
