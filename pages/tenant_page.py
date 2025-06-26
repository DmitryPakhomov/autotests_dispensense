class TenantPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть страницу Tenant (раздел Organisation в Management)"""
        pass

    def set_name(self, name: str):
        """Установить имя организации"""
        pass

    def set_description(self, description: str):
        """Установить описание организации"""
        pass

    def save_changes(self):
        """Нажать кнопку сохранения"""
        pass

    def should_see_success_message(self, message: str):
        """Проверить, что появилось сообщение об успешном обновлении"""
        pass

    def should_have_name(self, expected_name: str):
        """Проверить, что имя организации соответствует ожидаемому"""
        pass

    def should_have_description(self, expected_description: str):
        """Проверить, что описание соответствует ожидаемому"""
        pass

    def should_see_field_error(self, field: str, message: str):
        """Проверить, что возле поля отображается сообщение об ошибке"""
        pass

    def get_tenant_info(self) -> tuple[str, str]:
        """Получить имя и описание организации с формы"""
        return "Example Name", "Example Description"
