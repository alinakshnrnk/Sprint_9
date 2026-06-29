import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data.test_data import URLS


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
        self._dismiss_alert_if_present()

    def _dismiss_alert_if_present(self):
        try:
            self.wait.until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except Exception:
            pass

    @allure.step("Проверить, что открылась главная страница")
    def is_main_page_opened(self):
        try:
            self.wait.until(EC.url_contains("/recipes"))
            return True
        except Exception:
            return False

    @allure.step("Проверить, что кнопка 'Выход' отображается")
    def is_logout_button_visible(self):
        return self.is_visible(LoginPageLocators.LOGOUT_BUTTON)
