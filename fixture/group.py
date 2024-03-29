from model.models import Group


class GroupHelper:
    """Класс описывающий фикстуры объекта группа."""

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        """Метод открытия формы для создания новой группы."""
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and
                len(wd.find_elements_by_name('new')) > 0):
            # open group page
            wd.find_element_by_link_text('groups').click()

    def return_to_groups_page(self):
        """Метод. Переход на страницу со списком групп."""
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and
                len(wd.find_elements_by_name('new')) > 0):
            # open group page
            wd.find_element_by_link_text('group page').click()

    def selected_first_group(self):
        """Внутренний метод селект первой группы в списке."""
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def _selected_group_by_index(self, index):
        """Внутренний метод селект группы в списке по индексу."""
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def _selected_group_by_id(self, id):
        """Внутренний метод селект группы в списке по ID."""
        wd = self.app.wd
        wd.find_element_by_css_selector(f'input[value="{id}"]').click()

    def _change_field_value(self, field_name, text):
        """Внутренний метод. Выбор и заполнение указанного поля."""
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def _fill_group_form(self, group):
        """Внутренний метод заполнения полей формы группа."""
        wd = self.app.wd
        self._change_field_value('group_name', group.name)
        self._change_field_value('group_header', group.header)
        self._change_field_value('group_footer', group.footer)

    def count(self):
        """Метод определяет есть ли созданные группы."""
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name('selected[]'))

    def create(self, group):
        """
        Метод создания новой группы.
        Вызов метода открытия формы для создания новой группы.
        Фикстура заполнения полей формы группа и сохранения.
        Вызыв метода переход на страницу со списком групп.
        """
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name('new').click()
        # fill group form
        self._fill_group_form(group)
        # submit group creation
        wd.find_element_by_name('submit').click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        """ Метод удаление первой группы в списке."""
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        """
        Метод удаление указанной группы в списке.
        Открываем страницу со списком групп. Находим и удаляем
        группу в списке по индексу. Возвращаемся к списку групп.
        """
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self._selected_group_by_index(index)
        # submit and deletion
        wd.find_element_by_name('delete').click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        """
        Метод удаление указанной группы в списке.
        Открываем страницу со списком групп. Находим и удаляем
        группу в списке по ID. Возвращаемся к списку групп.
        """
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self._selected_group_by_id(id)
        # submit and deletion
        wd.find_element_by_name('delete').click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, new_group_date):
        """
        Метод изменения параметров первой группы.
        Открываем страницу со списком групп. Находим и изменяем
        указанные параметры выбранной группы. Возвращаемся к списку групп.
        """
        self.modify_group_by_index(0, new_group_date)

    def modify_group_by_index(self, index, new_group_date):
        """
        Метод изменения параметров указанной группы.
        Открываем страницу со списком групп. Находим и изменяем
        указанные параметры выбранной группы. Возвращаемся к списку групп.
        """
        wd = self.app.wd
        self.open_groups_page()
        self._selected_group_by_index(index)
        # open modification form group
        wd.find_element_by_name('edit').click()
        # fill group form
        self._fill_group_form(new_group_date)
        # submit modification
        wd.find_element_by_name('update').click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, id, new_group_date):
        """
        Метод изменения параметров группы.
        Открываем страницу со списком групп. Находим и изменяем
        передаваемые параметры группы по ID. Возвращаемся к списку групп.
        """
        wd = self.app.wd
        self.open_groups_page()
        self._selected_group_by_id(id)
        # open modification form group
        wd.find_element_by_name('edit').click()
        # fill group form
        self._fill_group_form(new_group_date)
        # submit modification
        wd.find_element_by_name('update').click()
        self.return_to_groups_page()
        self.group_cache = None

    # кэширование данных
    group_cache = None

    def get_group_list(self):
        """Метод сравнение списков групп."""
        self.group_cache = None
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []

            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name(
                        'selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))

        return list(self.group_cache)
