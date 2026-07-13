import allure
import pytest
from pages.registration_page import RegistrationPage


@allure.feature("Регистрация")
class TestRegistration:

    @allure.title("После регистрации происходит переход на страницу авторизации")
    @allure.description(
        "Открыть страницу регистрации, заполнить форму корректными данными "
        "и проверить, что произошёл переход на страницу авторизации."
    )
    @pytest.mark.registration
    def test_create_account_redirects_to_login(self, driver, registered_user):
        reg_page = RegistrationPage(driver)
        reg_page.open_registration_form()
        reg_page.fill_registration_form(
            registered_user["first_name"],
            registered_user["last_name"],
            registered_user["username"],
            registered_user["email"],
            registered_user["password"],
        )
        reg_page.submit_registration()

        assert reg_page.is_login_page_opened(), (
            "После регистрации не произошёл переход на страницу авторизации"
        )

    @allure.title("После регистрации отображается форма авторизации")
    @allure.description(
        "Открыть страницу регистрации, заполнить форму корректными данными "
        "и проверить, что на странице авторизации отображается форма входа."
    )
    @pytest.mark.registration
    def test_create_account_login_form_is_visible(self, driver, registered_user):
        reg_page = RegistrationPage(driver)
        reg_page.open_registration_form()
        reg_page.fill_registration_form(
            registered_user["first_name"],
            registered_user["last_name"],
            registered_user["username"],
            registered_user["email"],
            registered_user["password"],
        )
        reg_page.submit_registration()

        assert reg_page.is_login_form_visible(), (
            "После регистрации форма авторизации не отображается"
        )
