from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@name='last_name']")
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//form//button[not(@disabled)]")
    LOGIN_FORM = (By.XPATH,
                  "//form[.//input[@name='email'] and .//input[@name='password']]")
