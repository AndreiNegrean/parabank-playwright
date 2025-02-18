from playwright.sync_api import Page, Locator, expect
from support.user import User

LOGIN_PAGE_ERROR_TITLE = "ParaBank | Error"


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input: Locator = self.page.locator("input[name='username']")
        self.password_input: Locator = self.page.locator("input[name='password']")
        self.login_button: Locator = self.page.get_by_role("button", name="log in")
        self.failure_login_error_title_field: Locator = self.page.locator("#rightPanel .title", has_text="error")

    def navigate_to_login_page(self) -> None:
        self.page.goto("/parabank/login.htm")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_page_title(self):
        expect(self.page).to_have_title(LOGIN_PAGE_ERROR_TITLE)

    def assert_error_field_title(self):
        expect(self.failure_login_error_title_field).to_be_visible()
