from selenium.webdriver.common.by import By


class RecipePageLocators:
    CREATE_RECIPE_LINK = (By.XPATH, "//a[@href='/recipes/create']")

    RECIPE_NAME_INPUT = (By.XPATH,
                         "//div[contains(@class,'inputLabelText') and "
                         "normalize-space(text())='Название рецепта']"
                         "/parent::label/input")

    IMAGE_INPUT = (By.XPATH, "//input[@type='file']")

    ADD_INGREDIENT_BUTTON = (By.XPATH,
                             "//div[contains(@class,'ingredientAdd')]")

    INGREDIENT_INPUT = (By.XPATH,
                        "//input[contains(@class,'ingredientsInput')]")

    INGREDIENT_DROPDOWN_ITEM = (By.XPATH,
                                "//div[@class='styles_container__3ukwm']/div[1]")

    INGREDIENT_AMOUNT_INPUT = (By.XPATH,
                               "//input[contains(@class,'ingredientsAmountValue')]")

    INGREDIENT_ADDED_ITEM = (By.XPATH,
                             "//div[contains(@class,'ingredientsAddedItem')]")

    COOKING_TIME_INPUT = (By.XPATH,
                          "//div[contains(@class,'ingredientsTimeInput')]//input")

    DESCRIPTION_INPUT = (By.XPATH, "//textarea")

    SUBMIT_BUTTON_ACTIVE = (By.XPATH,
                            "//button[contains(., 'Создать рецепт') and not(@disabled)]")

    RECIPE_CARD = (By.XPATH,
                   "//h1[contains(@class,'single-card__title')]")

    RECIPE_CARD_TITLE = (By.XPATH,
                         "//h1[contains(@class,'single-card__title')]")
