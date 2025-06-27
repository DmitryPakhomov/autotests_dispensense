# Dispensense UI Test Automation

Автоматизированные UI-тесты для веб-приложения [Dispensense](https://app.stage.dispensense.ie/), написанные на Python с использованием Selenium, Pytest, Allure и Page Object паттерна.

---

## 📦 Стек

- Python 3.11+
- Selenium
- Pytest
- Allure
- Page Object Pattern
- uv (управление зависимостями)
- Git + PyCharm (рекомендуется)

---

## 📁 Структура проекта

```
project/
│
├── pages/               # Page Object классы
├── tests/               # Тесты
├── utils/               # Утилиты и конфигурации
├── config.py            # Настройки (BASE_URL, логин/пароль)
├── conftest.py          # Фикстуры Pytest
├── pyproject.toml       # Зависимости проекта (uv)
├── pytest.ini           # Настройки Pytest
└── README.md            # Документация
```

---

## ⚙️ Установка

1. Установите [uv](https://github.com/astral-sh/uv):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Установите зависимости:

```bash
uv venv
source .venv/bin/activate  # или .venv\Scripts\activate в Windows
uv pip install -r requirements.txt
```

---

## 🚀 Запуск тестов

### ✅ Полный запуск:

```bash
pytest --alluredir=allure-results
```

### ✅ Запуск с открытием браузера (не headless):

```bash
pytest --headed
```

### ✅ Запуск отдельного файла:

```bash
pytest tests/test_pharmacy_groups.py
```

---

## 📊 Allure отчёт

1. Установите Allure CLI:  
   https://docs.qameta.io/allure/#_installing_a_commandline

2. Сгенерируйте отчёт:

```bash
allure serve allure-results
```

---

## 🔐 Авторизация

Используется автологин через фикстуру `login`, которая берёт данные из `config.py`:

```python
EMAIL = "test-pharm4"
PASSWORD = "12345678"
BASE_URL = "https://app.stage.dispensense.ie/"
```

---

## ✍️ Автор

Создан в рамках автоматизации UI-тестирования проекта Dispensense.
