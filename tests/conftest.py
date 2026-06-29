import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.test_data import URLS


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
    browser.implicitly_wait(0)
    return browser


def _dismiss_alert(browser):
    try:
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        browser.switch_to.alert.accept()
    except Exception:
        pass


def _login(browser, username, password):
    wait = WebDriverWait(browser, 15)
    browser.get(URLS["login"])
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']")))
    browser.find_element(By.XPATH, "//input[@name='email']").send_keys(username)
    browser.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//form//button[not(@disabled)]"))).click()
    _dismiss_alert(browser)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Выход')]")))


@pytest.fixture(scope="function")
def driver(request):
    browser = _create_driver(request)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def existing_user_credentials(request):
    suffix = _random_string(8)
    user = {
        "first_name": "Auto",
        "last_name": "Tester",
        "username": f"auto_{suffix}",
        "email": f"auto_{suffix}@test.com",
        "password": "TestPass123!",
    }

    selenoid_url = request.config.getoption("--selenoid-url", default=None)
    if selenoid_url:
        setup_browser = webdriver.Remote(
            command_executor=selenoid_url,
            options=_get_chrome_options(selenoid=True),
        )
    else:
        setup_browser = webdriver.Chrome(options=_get_chrome_options())

    setup_browser.implicitly_wait(0)
    wait = WebDriverWait(setup_browser, 15)

    try:
        setup_browser.get(URLS["register"])
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='first_name']")))
        setup_browser.find_element(By.XPATH, "//input[@name='first_name']").send_keys(user["first_name"])
        setup_browser.find_element(By.XPATH, "//input[@name='last_name']").send_keys(user["last_name"])
        setup_browser.find_element(By.XPATH, "//input[@name='username']").send_keys(user["username"])
        setup_browser.find_element(By.XPATH, "//input[@name='email']").send_keys(user["email"])
        setup_browser.find_element(By.XPATH, "//input[@name='password']").send_keys(user["password"])
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//form//button[not(@disabled)]")
        )).click()
        wait.until(EC.url_contains("/signin"))
    finally:
        setup_browser.quit()

    return {"username": user["username"], "password": user["password"]}


@pytest.fixture(scope="function")
def authorized_driver(request, existing_user_credentials):
    browser = _create_driver(request)
    _login(browser, existing_user_credentials["username"], existing_user_credentials["password"])
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def registered_user():
    suffix = _random_string(6)
    return {
        "first_name": "Тест",
        "last_name": "Тестов",
        "username": f"user_{suffix}",
        "email": f"{suffix}@test.com",
        "password": "TestPass123!",
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
