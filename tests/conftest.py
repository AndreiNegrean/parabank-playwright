import os
import pytest
from dotenv import load_dotenv
from support.user import User
from support.utils import generate_fake_user
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.user_dashboard_page import UserDashboardPage
from playwright.sync_api import Page

load_dotenv("../.env")


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL")


@pytest.fixture
def register_page(page) -> RegisterPage:
    return RegisterPage(page)


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def user_dashboard_page(page) -> UserDashboardPage:
    return UserDashboardPage(page)


@pytest.fixture(scope="session")
def valid_user() -> User:
    return generate_fake_user(valid_user=True)


@pytest.fixture(scope="session")
def invalid_user() -> User:
    return generate_fake_user(valid_user=False)





