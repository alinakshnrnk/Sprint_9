import random
import string
from pathlib import Path

BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru"

URLS = {
    "main": BASE_URL + "/",
    "login": BASE_URL + "/signin",
    "register": BASE_URL + "/signup",
    "recipes": BASE_URL + "/recipes",
    "recipe_create": BASE_URL + "/recipes/create",
}

APP_DIR = Path(__file__).parent.parent

RECIPE_IMAGE_PATH = str(APP_DIR / "data" / "files" / "test_image.jpg")
