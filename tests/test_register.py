from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from pages.user_dashboard_page import UserDashboardPage
from support.user import User


def test_successful_register(page: Page, register_page: RegisterPage, valid_user: User):
    # Given the register page is displayed
    register_page.navigate_to_register_page()

    # When the user register with valid credentials
    register_page.register(first_name=valid_user.first_name, last_name=valid_user.last_name, address=valid_user.address,
                           city=valid_user.city, state=valid_user.state, zip_code=valid_user.zip_code, phone=valid_user.phone,
                           ssn=valid_user.ssn, username=valid_user.username, password=valid_user.password)

    # Then the elements indicative of a successful registration are present
    register_page.assert_successful_registration_page_title()
    register_page.assert_successful_registration_welcome_message(valid_user.username)
    register_page.assert_successful_registration_message()


def test_failure_register(page: Page, register_page: RegisterPage, invalid_user: User):
    # Given the register page is displayed
    register_page.navigate_to_register_page()

    # When the user register with invalid credentials
    register_page.register(first_name=invalid_user.first_name, last_name=invalid_user.last_name,
                           address=invalid_user.address, city=invalid_user.city, state=invalid_user.state,
                           zip_code=invalid_user.zip_code, phone=invalid_user.phone, ssn=invalid_user.ssn,
                           username=invalid_user.username, password=invalid_user.password)

    # Then the elements indicative of a failure registration are present
    register_page.assert_failure_registration_error_message()
    register_page.assert_failure_registration_successful_message_not_present()
