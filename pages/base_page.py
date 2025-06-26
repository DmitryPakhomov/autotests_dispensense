from utils.config import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path: str):
        """Открыть страницу по относительному пути от BASE_URL"""
        url = BASE_URL.rstrip("/") + "/" + path.lstrip("/")
        self.driver.get(url)
