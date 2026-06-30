import pytest

from tests.helpers import (
    build_new_user,
    build_recipe_data,
    create_driver,
    log_in_user,
    register_new_user,
)


def pytest_addoption(parser):
    parser.addoption(
        "--selenoid-url",
        action="store",
        default=None,
        help="URL Selenoid, например http://selenoid:4444/wd/hub",
    )


@pytest.fixture(scope="function")
def driver(request):
    selenoid_url = request.config.getoption("--selenoid-url")
    browser = create_driver(selenoid_url)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def existing_user_credentials(driver):
    user = build_new_user(username_prefix="auto")
    register_new_user(driver, user)
    return {"username": user["username"], "password": user["password"]}


@pytest.fixture(scope="function")
def authorized_driver(driver, existing_user_credentials):
    log_in_user(
        driver,
        existing_user_credentials["username"],
        existing_user_credentials["password"],
    )
    return driver


@pytest.fixture(scope="function")
def registered_user():
    return build_new_user(username_prefix="user")


@pytest.fixture(scope="function")
def recipe_data():
    return build_recipe_data()
