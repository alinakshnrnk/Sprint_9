import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators
from data.test_data import URLS


class RegistrationPage(BasePage):

    @allure.step("Открыть страницу регистрации")
    def open_registration_form(self):
        self.open(URLS["register"])

    @allure.step("Заполнить форму регистрации")
    def fill_registration_form(self, first_name, last_name, username, email, password):
        self.enter_text(RegistrationPageLocators.FIRST_NAME_INPUT, first_name)
        self.enter_text(RegistrationPageLocators.LAST_NAME_INPUT, last_name)
        self.enter_text(RegistrationPageLocators.USERNAME_INPUT, username)
        self.enter_text(RegistrationPageLocators.EMAIL_INPUT, email)
        self.enter_text(RegistrationPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку 'Создать аккаунт'")
    def submit_registration(self):
        self.click(RegistrationPageLocators.SUBMIT_BUTTON)

    @allure.step("Проверить, что открылась страница авторизации")
    def is_login_page_opened(self):
        try:
            self.wait_for_url("/signin")
            return True
        except Exception:
            return False

    @allure.step("Проверить, что форма авторизации отображается")
    def is_login_form_visible(self):
        return self.is_visible(RegistrationPageLocators.LOGIN_FORM)

    @allure.step("Зарегистрировать пользователя")
    def register_user(self, first_name, last_name, username, email, password):
        self.open_registration_form()
        self.fill_registration_form(first_name, last_name, username, email, password)
        self.submit_registration()
        self.wait_for_url("/signin")
