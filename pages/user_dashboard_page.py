from playwright.sync_api import Page, Locator, expect
from support.user import User

EXPECTED_USER_DASHBOARD_PAGE_TITLE = "ParaBank | Accounts Overview"


class UserDashboardPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = self.page.title()
        self.accounts_overview_field: Locator = self.page.get_by_text(f"accounts overview")
        self.dashboard_welcome_field: Locator = self.page.locator("#leftPanel", has_text="welcome")

    def navigate_to_user_dashboard_page(self):
        self.page.goto("/parabank/overview.htm")

    def assert_user_dashboard_page_title(self) -> None:
        expect(self.page).to_have_title(EXPECTED_USER_DASHBOARD_PAGE_TITLE)

    def assert_user_dashboard_welcome_message(self, user_first_name: str, user_last_name: str) -> None:
        expect(self.dashboard_welcome_field).to_contain_text(user_first_name)
        expect(self.dashboard_welcome_field).to_contain_text(user_last_name)

