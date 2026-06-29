import allure
import pytest
from pages.login_page import LoginPage


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Успешная авторизация переводит на главную страницу")
    @allure.description(
        "Открыть страницу авторизации, заполнить форму корректными данными "
        "и проверить, что произошёл переход на главную страницу."
    )
    @pytest.mark.login
    def test_login_redirects_to_main_page(self, driver, existing_user_credentials):
        login_page = LoginPage(driver)
        login_page.open_login_form()
        login_page.fill_login_form(
            existing_user_credentials["username"],
            existing_user_credentials["password"],
        )
        login_page.submit_login()

        assert login_page.is_main_page_opened(), (
            "После авторизации не произошёл переход на главную страницу"
        )

    @allure.title("После авторизации отображается кнопка 'Выход'")
    @allure.description(
        "Открыть страницу авторизации, заполнить форму корректными данными "
        "и проверить, что кнопка 'Выход' отображается в навигации."
    )
    @pytest.mark.login
    def test_login_shows_logout_button(self, driver, existing_user_credentials):
        login_page = LoginPage(driver)
        login_page.open_login_form()
        login_page.fill_login_form(
            existing_user_credentials["username"],
            existing_user_credentials["password"],
        )
        login_page.submit_login()

        assert login_page.is_logout_button_visible(), (
            "После авторизации кнопка 'Выход' не отображается"
        )
