class DevicePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть страницу устройств через меню управления"""
        pass

    def add_device(self, name: str):
        """Добавить устройство с заданным именем"""
        pass

    def should_see_device(self, name: str):
        """Проверить, что устройство отображается в таблице"""
        pass

    def edit_device(self, old_name: str, new_name: str):
        """Отредактировать устройство с новым именем"""
        pass

    def apply_filter(self, keyword: str):
        """Применить фильтр по ключевому слову"""
        pass

    def should_see_filtered_results(self, keyword: str):
        """Проверить, что отфильтрованные устройства соответствуют ключу"""
        pass

    def open_add_device_dialog(self):
        """Открыть диалог добавления устройства"""
        pass

    def save_without_required_fields(self):
        """Попробовать сохранить форму без обязательных полей"""
        pass

    def should_see_validation_errors(self):
        """Проверить, что ошибки валидации отображаются"""
        pass

    def logout(self):
        """Выйти из текущего пользователя"""
        pass

    def should_see_devices_button(self):
        """Проверить, что кнопка 'Devices' видна в боковом меню"""
        pass
