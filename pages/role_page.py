class RolePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть страницу ролей"""
        pass

    def create_role(self, name: str):
        """Создать роль с заданным именем"""
        pass

    def should_see_role(self, name: str):
        """Убедиться, что роль отображается в списке"""
        pass

    def delete_role(self, name: str):
        """Удалить роль"""
        pass

    def should_not_see_role(self, name: str):
        """Убедиться, что роль удалена"""
        pass

    def logout(self):
        """Выйти из аккаунта"""
        pass

    def should_not_see_role_button(self):
        """Проверить отсутствие кнопки ролей"""
        pass
