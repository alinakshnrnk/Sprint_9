FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей Chrome
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Команда по умолчанию: запуск тестов через Selenoid
CMD ["pytest", "tests/", "--selenoid-url=http://selenoid:4444/wd/hub", "-v", "--alluredir=allure-results"]
