class PharmacyGroupPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть основную страницу группы аптек"""
        pass

    def open_default_group(self):
        """Открыть дефолтную аптечную группу"""
        pass

    def should_not_see_delete_button(self):
        """Проверить, что кнопка 'удалить' не отображается"""
        pass

    def should_not_see_delete_icon_near_pharmacies(self):
        """Проверить, что нет иконки удаления рядом с аптеками"""
        pass

    def mark_as_default(self):
        """Установить текущую группу как дефолтную"""
        pass

    def save_changes(self):
        """Сохранить изменения"""
        pass

    def should_be_default(self):
        """Убедиться, что текущая группа стала дефолтной"""
        pass

    def previous_default_should_not_be_default(self):
        """Проверить, что старая дефолтная группа больше не дефолтная"""
        pass

    def navigate_to_groups(self):
        """Навигация к списку групп"""
        pass

    def delete_group(self, confirm=False):
        """Удалить текущую группу"""
        pass

    def should_be_deleted(self):
        """Убедиться, что группа была удалена"""
        pass

    def add_pharmacy(self, name):
        """Добавить аптеку в текущую группу"""
        pass

    def should_be_default_group(self, pharmacy_name):
        """Убедиться, что аптека теперь в дефолтной группе"""
        pass

    def open_section(self):
        """Открыть раздел групп аптек"""
        pass

    def search(self, query):
        """Ввести поисковый запрос"""
        pass

    def should_show_result(self, result):
        """Проверить, что поиск отобразил нужную группу"""
        pass

    def select_result(self, name):
        """Выбрать группу из результатов поиска"""
        pass

    def should_open_group(self, name):
        """Убедиться, что нужная группа открыта"""
        pass

    def create_group(self, name, pharmacies):
        """Создать группу с аптеками"""
        pass

    def should_see_group(self, name):
        """Убедиться, что группа с таким именем отображается"""
        pass

    def add_pharmacy_from_other_group(self, name):
        """Добавить аптеку, которая уже в другой группе"""
        pass

    def confirm_change_group(self):
        """Подтвердить изменение группы аптеки"""
        pass

    def should_show_group_updated_message(self):
        """Проверить сообщение об успешном обновлении"""
        pass

    def delete_pharmacy(self, name):
        """Удалить аптеку из текущей группы"""
        pass

    def go_back(self):
        """Нажать кнопку 'назад' в хлебных крошках"""
        pass

    def open_again(self):
        """Повторно открыть группу"""
        pass

    def should_see_group_empty(self):
        """Убедиться, что группа пуста"""
        pass

    def should_see_pharmacies(self, pharmacies):
        """Убедиться, что список аптек соответствует ожиданиям"""
        pass

    def set_as_default(self):
        """Установить группу как дефолтную"""
        pass

    def go_to_pharmacies(self):
        """Перейти к разделу аптек"""
        pass

    def create_pharmacy(self, name):
        """Создать аптеку с заданным именем"""
        pass

    def should_see_pharmacy(self, name):
        """Проверить, что аптека отображается в списке"""
        pass
