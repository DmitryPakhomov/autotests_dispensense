class PharmacyPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть раздел аптек"""
        pass

    def create_pharmacy(self, name: str):
        """Создать аптеку с заданным именем"""
        pass

    def open_pharmacy(self, name: str):
        """Открыть карточку аптеки по имени"""
        pass

    def should_see_pharmacy(self, name: str):
        """Убедиться, что аптека отображается в списке или карточке"""
        pass

    def edit_pharmacy(self, old_name: str, new_name: str):
        """Отредактировать имя аптеки"""
        pass

    def open_integrations_tab(self):
        """Открыть вкладку интеграций аптеки"""
        pass

    def add_integration(self, name: str):
        """Добавить интеграцию"""
        pass

    def edit_integration(self, old_name: str, new_name: str):
        """Переименовать или изменить интеграцию"""
        pass

    def should_see_integration(self, name: str):
        """Убедиться, что интеграция отображается"""
        pass

    def open_ordering_tab(self):
        """Открыть вкладку заказа поставок"""
        pass

    def add_supplier_integration(self, name: str):
        """Добавить поставщика интеграции"""
        pass

    def remove_supplier_integration(self, name: str):
        """Удалить интеграцию поставщика"""
        pass

    def enable_integration(self, name: str):
        """Включить интеграцию"""
        pass

    def should_see_enabled_integration(self, name: str):
        """Проверить, что интеграция включена"""
        pass

    def should_see_ordering_tab_empty(self):
        """Проверить, что вкладка заказа пустая"""
        pass

    def open_contact_tab(self):
        """Открыть вкладку контактной информации"""
        pass

    def fill_invalid_contact_details(self):
        """Заполнить некорректные данные (email, телефон)"""
        pass

    def fill_contact_details(self, email: str, phone: str):
        """Заполнить корректные контактные данные"""
        pass

    def should_see_contact_validation_errors(self):
        """Проверить отображение ошибок валидации"""
        pass

    def should_see_saved_contact_details(self):
        """Проверить, что контактные данные успешно сохранены"""
        pass

    def open_employees_tab(self):
        """Открыть вкладку сотрудников в аптеке"""
        pass

    def add_employee(self, name: str, role: str):
        """Добавить сотрудника к аптеке"""
        pass

    def delete_employee(self, name: str):
        """Удалить сотрудника из аптеки"""
        pass

    def should_see_employee(self, name: str):
        """Проверить, что сотрудник отображается на вкладке"""
        pass

    def should_see_employees_tab_empty(self):
        """Проверить, что вкладка сотрудников пуста"""
        pass

    def logout(self):
        """Выйти из аккаунта"""
        pass

    def should_see_pharmacy_button_in_menu(self):
        """Проверить доступность кнопки 'Pharmacy' в меню"""
        pass
