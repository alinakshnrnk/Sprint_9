import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data.test_data import URLS, DEFAULT_USER


def _random_string(length=8):
    return "".join(random.choices(string.ascii_lowercase, k=length))


def _get_chrome_options(selenoid=False):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if selenoid:
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "126.0")
        options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": False})
    return options


def _create_driver(request):
    selenoid_url = request.config.getoption("--selenoid-url", default=None)
    if selenoid_url:
        browser = webdriver.Remote(
            command_executor=selenoid_url,
            options=_get_chrome_options(selenoid=True),
        )
    else:
        browser = webdriver.Chrome(options=_get_chrome_options())
    return browser


@pytest.fixture(scope="function")
def driver(request):
    browser = _create_driver(request)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def existing_user_credentials(request):
    from pages.registration_page import RegistrationPage

    suffix = _random_string(8)
    user = {
        "first_name": DEFAULT_USER["first_name"],
        "last_name": DEFAULT_USER["last_name"],
        "username": f"auto_{suffix}",
        "email": f"auto_{suffix}@test.com",
        "password": DEFAULT_USER["password"],
    }

    selenoid_url = request.config.getoption("--selenoid-url", default=None)
    if selenoid_url:
        setup_browser = webdriver.Remote(
            command_executor=selenoid_url,
            options=_get_chrome_options(selenoid=True),
        )
    else:
        setup_browser = webdriver.Chrome(options=_get_chrome_options())

    try:
        reg_page = RegistrationPage(setup_browser)
        reg_page.register_user(
            user["first_name"],
            user["last_name"],
            user["username"],
            user["email"],
            user["password"],
        )
    finally:
        setup_browser.quit()

    return {"username": user["username"], "password": user["password"]}


@pytest.fixture(scope="function")
def authorized_driver(request, existing_user_credentials):
    from pages.login_page import LoginPage

    browser = _create_driver(request)
    login_page = LoginPage(browser)
    login_page.open_login_form()
    login_page.fill_login_form(
        existing_user_credentials["username"],
        existing_user_credentials["password"],
    )
    login_page.submit_login()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def registered_user():
    suffix = _random_string(6)
    return {
        "first_name": DEFAULT_USER["first_name"],
        "last_name": DEFAULT_USER["last_name"],
        "username": f"user_{suffix}",
        "email": f"{suffix}@test.com",
        "password": DEFAULT_USER["password"],
    }


@pytest.fixture(scope="function")
def recipe_data():
    from data.test_data import RECIPE_IMAGE_PATH
    suffix = _random_string(4)
    return {
        "name": f"Тестовый рецепт {suffix}",
        "ingredient": "картофель",
        "ingredient_amount": "200",
        "cooking_time": "10",
        "description": "Тестовое описание рецепта",
        "image_path": RECIPE_IMAGE_PATH,
    }


def pytest_addoption(parser):
    parser.addoption(
        "--selenoid-url",
        action="store",
        default=None,
        help="URL Selenoid, например http://selenoid:4444/wd/hub",
    )
