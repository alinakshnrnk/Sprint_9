import allure
import pytest
from pages.recipe_page import RecipePage


@allure.feature("Создание рецепта")
class TestRecipeCreation:

    @allure.title("Карточка созданного рецепта отображается")
    @allure.description(
        "Авторизоваться, перейти на страницу создания рецепта, заполнить все поля "
        "и проверить, что после сохранения страница рецепта открылась."
    )
    @pytest.mark.recipe
    def test_created_recipe_card_is_visible(self, authorized_driver, recipe_data):
        recipe_page = RecipePage(authorized_driver)
        recipe_page.open_create_recipe_tab()
        recipe_page.enter_recipe_name(recipe_data["name"])
        recipe_page.upload_image(recipe_data["image_path"])
        recipe_page.add_ingredient(recipe_data["ingredient"], recipe_data["ingredient_amount"])
        recipe_page.enter_cooking_time(recipe_data["cooking_time"])
        recipe_page.enter_description(recipe_data["description"])
        recipe_page.submit_recipe()

        assert recipe_page.is_recipe_card_visible(), (
            "Карточка созданного рецепта не отображается"
        )

    @allure.title("Название созданного рецепта совпадает с введённым")
    @allure.description(
        "Авторизоваться, перейти на страницу создания рецепта, заполнить все поля "
        "и проверить, что название рецепта совпадает с введённым."
    )
    @pytest.mark.recipe
    def test_created_recipe_card_has_correct_title(self, authorized_driver, recipe_data):
        recipe_page = RecipePage(authorized_driver)
        recipe_page.open_create_recipe_tab()
        recipe_page.enter_recipe_name(recipe_data["name"])
        recipe_page.upload_image(recipe_data["image_path"])
        recipe_page.add_ingredient(recipe_data["ingredient"], recipe_data["ingredient_amount"])
        recipe_page.enter_cooking_time(recipe_data["cooking_time"])
        recipe_page.enter_description(recipe_data["description"])
        recipe_page.submit_recipe()

        assert recipe_page.get_recipe_card_title() == recipe_data["name"], (
            f"Название рецепта не совпадает: ожидалось '{recipe_data['name']}'"
        )
