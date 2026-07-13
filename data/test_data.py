from pathlib import Path

APP_DIR = Path(__file__).parent.parent

RECIPE_IMAGE_PATH = str(APP_DIR / "data" / "files" / "test_image.jpg")

DEFAULT_USER = {
    "first_name": "Тест",
    "last_name": "Тестов",
    "password": "TestPass123!",
}
