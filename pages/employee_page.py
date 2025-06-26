class EmployeePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть раздел сотрудников"""
        pass

    def create_employee(self, role: str, pharmacy: str):
        """Создать нового сотрудника с ролью и аптекой"""
        pass

    def search_employee(self, name: str):
        """Найти сотрудника по имени"""
        pass

    def should_see_employee(self, name: str):
        """Проверить, что сотрудник отображается в списке"""
        pass

    def edit_employee(self, name: str, new_role: str):
        """Изменить роль у существующего сотрудника"""
        pass

    def should_see_employee_with_role(self, name: str, role: str):
        """Проверить, что сотрудник отображается с нужной ролью"""
        pass

    def delete_employee(self, name: str):
        """Удалить сотрудника"""
        pass

    def filter_deleted(self):
        """Фильтровать по удалённым сотрудникам"""
        pass

    def restore_employee(self, name: str):
        """Восстановить удалённого сотрудника"""
        pass

    def reset_filter(self):
        """Сбросить фильтры"""
        pass

    def reinvite_employee(self, name: str):
        """Повторно пригласить сотрудника"""
        pass

    def should_see_reinvite_success(self, name: str):
        """Проверить, что приглашение было отправлено успешно"""
        pass

    def logout(self):
        """Выйти из текущего пользователя"""
        pass

    def should_see_employees_button(self):
        """Проверить доступность кнопки 'Employees'"""
        pass

    def go_to_employees_page(self):
        """Перейти на страницу сотрудников"""
        pass

    def should_not_see_edit_button(self, name: str):
        """Убедиться, что кнопка редактирования не отображается"""
        pass

    def should_not_see_delete_button(self, name: str):
        """Убедиться, что кнопка удаления не отображается"""
        pass

    def should_not_see_add_button(self):
        """Убедиться, что кнопка добавления нового сотрудника отсутствует"""
        pass

    def go_to_deleted_employees(self):
        """Перейти к удалённым сотрудникам"""
        pass

    def should_not_see_restore_button(self, name: str):
        """Проверить, что кнопка восстановления не отображается"""
        pass
