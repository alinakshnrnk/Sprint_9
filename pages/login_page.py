import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data.urls import URLS


class LoginPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open_login_form(self):
        self.open(URLS["login"])

    @allure.step("Заполнить форму авторизации")
    def fill_login_form(self, username, password):
        self.enter_text(LoginPageLocators.EMAIL_INPUT, username)
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку 'Войти'")
    def submit_login(self):
        self.click(LoginPageLocators.SUBMIT_BUTTON)
        self.dismiss_alert_if_present()

    @allure.step("Проверить, что открылась главная страница")
    def is_main_page_opened(self):
        try:
            self.wait_for_url("/recipes")
            return True
        except Exception:
            return False

    @allure.step("Проверить, что кнопка 'Выход' отображается")
    def is_logout_button_visible(self):
        return self.is_visible(LoginPageLocators.LOGOUT_BUTTON)
