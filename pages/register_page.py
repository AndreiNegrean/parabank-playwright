from playwright.sync_api import Page, Locator, expect

EXPECTED_SUCCESSFUL_REGISTRATION_TITLE = "ParaBank | Customer Created"
SUCCESSFUL_REGISTRATION_MESSAGE = f"Your account was created successfully. You are now logged in."


class RegisterPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_name_input: Locator = self.page.locator("input[name='customer.firstName']")
        self.last_name_input: Locator = self.page.locator("input[name='customer.lastName']")
        self.address_input: Locator = self.page.locator("input[name='customer.address.street']")
        self.city_input: Locator = self.page.locator("input[name='customer.address.city']")
        self.state_input: Locator = self.page.locator("input[name='customer.address.state']")
        self.zip_code_input: Locator = self.page.locator("input[name='customer.address.zipCode']")
        self.phone_input: Locator = self.page.locator("input[name='customer.phoneNumber']")
        self.ssn_input: Locator = self.page.locator("input[name='customer.ssn']")
        self.username_input: Locator = self.page.locator("input[name='customer.username']")
        self.password_input: Locator = self.page.locator("input[name='customer.password']")
        self.password_confirm_input: Locator = self.page.locator("input[name='repeatedPassword']")
        self.register_button: Locator = self.page.get_by_role("button", name="register")

        self.successful_registration_welcome_field: Locator = self.page.locator("#rightPanel", has_text="welcome")
        self.successful_registration_message_field: Locator = self.page.get_by_text(SUCCESSFUL_REGISTRATION_MESSAGE)
        self.failure_registration_error_message_field: Locator = self.page.locator("#rightPanel .error").first

    def navigate_to_register_page(self) -> None:
        self.page.goto("/parabank/register.htm")

    def register(self, first_name: str, last_name: str, address: str, city: str, state: str, zip_code: str, phone: str,
                 ssn: str, username: str, password: str) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.address_input.fill(address)
        self.city_input.fill(city)
        self.state_input.fill(state)
        self.zip_code_input.fill(zip_code)
        self.phone_input.fill(phone)
        self.ssn_input.fill(ssn)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.password_confirm_input.fill(password)
        self.register_button.click()

    def assert_successful_registration_page_title(self) -> None:
        expect(self.page).to_have_title(EXPECTED_SUCCESSFUL_REGISTRATION_TITLE)

    def assert_successful_registration_welcome_message(self, username: str) -> None:
        expect(self.successful_registration_welcome_field).to_contain_text(username)

    def assert_successful_registration_message(self) -> None:
        expect(self.successful_registration_message_field).to_be_visible()

    def assert_failure_registration_error_message(self) -> None:
        expect(self.failure_registration_error_message_field).to_be_visible()

    def assert_failure_registration_successful_message_not_present(self) -> None:
        expect(self.successful_registration_message_field).not_to_be_visible()
