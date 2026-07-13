import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.test_data import DEFAULT_USER, RECIPE_IMAGE_PATH
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


def generate_random_string(length=8):
    return "".join(random.choices(string.ascii_lowercase, k=length))


def build_chrome_options(selenoid=False):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if selenoid:
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "126.0")
        options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": False})
    return options


def create_driver(selenoid_url=None):
    if selenoid_url:
        return webdriver.Remote(
            command_executor=selenoid_url,
            options=build_chrome_options(selenoid=True),
        )
    return webdriver.Chrome(options=build_chrome_options())


def build_new_user(username_prefix="user"):
    suffix = generate_random_string(8)
    return {
        "first_name": DEFAULT_USER["first_name"],
        "last_name": DEFAULT_USER["last_name"],
        "username": f"{username_prefix}_{suffix}",
        "email": f"{username_prefix}_{suffix}@test.com",
        "password": DEFAULT_USER["password"],
    }


def register_new_user(driver, user):
    reg_page = RegistrationPage(driver)
    reg_page.register_user(
        user["first_name"],
        user["last_name"],
        user["username"],
        user["email"],
        user["password"],
    )


def log_in_user(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_login_form(username, password)
    login_page.submit_login()


def build_recipe_data():
    suffix = generate_random_string(4)
    return {
        "name": f"Тестовый рецепт {suffix}",
        "ingredient": "картофель",
        "ingredient_amount": "200",
        "cooking_time": "10",
        "description": "Тестовое описание рецепта",
        "image_path": RECIPE_IMAGE_PATH,
    }
