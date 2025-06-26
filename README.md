# UI Automation Project

This project contains automated UI tests using **pytest**, **selenium**, and **allure-pytest**.

## Project Structure

- `tests/` – test files using Page Object pattern
- `pages/` – Page Object classes encapsulating UI logic
- `utils/` – utilities such as driver setup
- `conftest.py` – driver fixture
- `requirements.txt` – dependencies

## Getting Started

```bash
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve allure-results
