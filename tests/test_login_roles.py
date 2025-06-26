import pytest
import allure


@allure.suite("Management tests")
@allure.feature("Employees")
@allure.title("Allow to login for each employee role by email/pass")
def test_login_all_roles(login):
    credentials = [
        ("testadmin@gmail.com", "TestAdmin"),
        ("testpharmacist@gmail.com", "TestPharmacist"),
        ("headofficemanager@gmail.com", "TestHeadOfficeManager"),
        ("pharmacyowner@gmail.com", "TestPharmacyOwner"),
        ("technician@gmail.com", "TestTechnician"),
        ("FOSStaff@gmail.com", "TestFOSStaff"),
        ("FOSManager@gmail.com", "TestFOSManager"),
        ("mrgrindewald@testtest.tt", "MrGrindewald"),
        ("testclaimsuser@gmail.com", "TestClaimsUser")
    ]
    for email, expected_name in credentials:
        login.login(email=email, password="password123")  # временно здесь — т.к. фикстура login возвращает LoginPage
        login.should_see_username(expected_name)
        login.logout()
