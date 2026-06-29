import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators
from data.test_data import URLS


class RecipePage(BasePage):

    @allure.step("Перейти на страницу создания рецепта")
    def open_create_recipe_tab(self):
        self.open(URLS["recipe_create"])

    @allure.step("Ввести название рецепта")
    def enter_recipe_name(self, name):
        self.enter_text(RecipePageLocators.RECIPE_NAME_INPUT, name)

    @allure.step("Загрузить изображение рецепта")
    def upload_image(self, image_path):
        self.find_element(RecipePageLocators.IMAGE_INPUT).send_keys(image_path)

    @allure.step("Добавить ингредиент")
    def add_ingredient(self, ingredient, amount):
        input_el = self.find_element(RecipePageLocators.INGREDIENT_INPUT)
        input_el.click()
        for char in ingredient:
            input_el.send_keys(char)
            self.wait.until(lambda d: input_el.get_attribute("value") != "")

        self.wait.until(
            EC.visibility_of_element_located(RecipePageLocators.INGREDIENT_DROPDOWN_ITEM)
        )
        self.click(RecipePageLocators.INGREDIENT_DROPDOWN_ITEM)

        self.wait.until(
            EC.visibility_of_element_located(RecipePageLocators.INGREDIENT_AMOUNT_INPUT)
        )
        self.enter_text(RecipePageLocators.INGREDIENT_AMOUNT_INPUT, amount)

        add_btn = self.find_element(RecipePageLocators.ADD_INGREDIENT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
        self.driver.execute_script("arguments[0].click();", add_btn)

        self.wait.until(
            EC.visibility_of_element_located(RecipePageLocators.INGREDIENT_ADDED_ITEM)
        )

    @allure.step("Ввести время приготовления")
    def enter_cooking_time(self, cooking_time):
        self.enter_text(RecipePageLocators.COOKING_TIME_INPUT, cooking_time)

    @allure.step("Ввести описание рецепта")
    def enter_description(self, description):
        self.enter_text(RecipePageLocators.DESCRIPTION_INPUT, description)

    @allure.step("Нажать кнопку 'Создать рецепт'")
    def submit_recipe(self):
        self.wait.until(
            EC.element_to_be_clickable(RecipePageLocators.SUBMIT_BUTTON_ACTIVE)
        )
        button = self.find_element(RecipePageLocators.SUBMIT_BUTTON_ACTIVE)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
        self.wait.until(EC.url_contains("/recipes/"))

    @allure.step("Проверить, что страница рецепта открылась")
    def is_recipe_card_visible(self):
        return self.is_visible(RecipePageLocators.RECIPE_CARD)

    @allure.step("Получить название рецепта со страницы")
    def get_recipe_card_title(self):
        return self.get_text(RecipePageLocators.RECIPE_CARD_TITLE)
