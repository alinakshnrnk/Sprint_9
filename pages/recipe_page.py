import allure
from pages.base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators
from data.urls import URLS


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

        self.find_visible(RecipePageLocators.INGREDIENT_DROPDOWN_ITEM)
        self.click(RecipePageLocators.INGREDIENT_DROPDOWN_ITEM)

        self.find_visible(RecipePageLocators.INGREDIENT_AMOUNT_INPUT)
        self.enter_text(RecipePageLocators.INGREDIENT_AMOUNT_INPUT, amount)

        self.js_click(RecipePageLocators.ADD_INGREDIENT_BUTTON)
        self.find_visible(RecipePageLocators.INGREDIENT_ADDED_ITEM)

    @allure.step("Ввести время приготовления")
    def enter_cooking_time(self, cooking_time):
        self.enter_text(RecipePageLocators.COOKING_TIME_INPUT, cooking_time)

    @allure.step("Ввести описание рецепта")
    def enter_description(self, description):
        self.enter_text(RecipePageLocators.DESCRIPTION_INPUT, description)

    @allure.step("Нажать кнопку 'Создать рецепт'")
    def submit_recipe(self):
        self.js_click(RecipePageLocators.SUBMIT_BUTTON_ACTIVE)
        self.wait_for_url("/recipes/")

    @allure.step("Проверить, что страница рецепта открылась")
    def is_recipe_card_visible(self):
        return self.is_visible(RecipePageLocators.RECIPE_CARD)

    @allure.step("Получить название рецепта со страницы")
    def get_recipe_card_title(self):
        return self.get_text(RecipePageLocators.RECIPE_CARD_TITLE)
