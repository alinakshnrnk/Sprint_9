from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//form//button[not(@disabled)]")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(),'Выход')]")
    MAIN_PAGE_RECIPES_HEADER = (By.XPATH, "//h1[contains(text(),'Рецепты')]")
