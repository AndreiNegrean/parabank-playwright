from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.user_dashboard_page import UserDashboardPage
from support.user import User


def test_successful_login(page: Page, login_page: LoginPage, user_dashboard_page: UserDashboardPage, valid_user: User):
    # Given the login page is displayed
    login_page.navigate_to_login_page()

    # When the user logs into the app with valid credentials
    login_page.login(username=valid_user.username, password=valid_user.password)

    # Then the elements indicative of a logged-in state are present
    user_dashboard_page.assert_user_dashboard_page_title()
    user_dashboard_page.assert_user_dashboard_welcome_message(valid_user.first_name, valid_user.last_name)


def test_failure_login(page: Page, login_page: LoginPage, invalid_user: User):
    # Given the login page is displayed
    login_page.navigate_to_login_page()

    # When the user logs into the app with invalid credentials
    login_page.login(username=invalid_user.username, password=invalid_user.password)

    # Then the elements indicative of an error state are present
    login_page.assert_error_page_title()
    login_page.assert_error_field_title()
    login_page.assert_error_field_message()
