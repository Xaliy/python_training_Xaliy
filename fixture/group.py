class GroupHelper:
    """Класс описывающий фикстуры объекта группа."""

    def __init__(self, app):
        self.app = app

    def open_groups(self):
        """Метод открытия формы для создания новой группы."""
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        """
        Метод создания новой группы.
        Вызов метода открытия формы для создания новой группы.
        Фикстура заполнения полей формы группа и сохранения.
        Вызыв метода переход на страницу со списком групп.
        """
        wd = self.app.wd
        self.open_groups()
        # init group creation
        wd.find_element_by_name('new').click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name('submit').click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        """Внутренний метод заполнения полей формы группа."""
        wd = self.app.wd
        self.change_field_value('group_name', group.name)
        self.change_field_value('group_header', group.header)
        self.change_field_value('group_footer', group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit(self, group):
        """
        Метод редактирование группы.
        Вызов метода открытия формы для создания новой группы.
        Фикстура заполнения полей формы группа и сохранения.
        Вызыв метода переход на страницу со списком групп.
        """
        wd = self.app.wd
        self.open_groups()
        # select first group
        wd.find_element_by_name('selected[]').click()
        # button edit
        wd.find_element_by_name('edit').click()
        # fill group form
        wd.find_element_by_name('group_name').click()
        wd.find_element_by_name('group_name').clear()
        wd.find_element_by_name('group_name').send_keys(group.name)
        wd.find_element_by_name('group_header').click()
        wd.find_element_by_name('group_header').clear()
        wd.find_element_by_name('group_header').send_keys(group.header)
        wd.find_element_by_name('group_footer').click()
        wd.find_element_by_name('group_footer').clear()
        wd.find_element_by_name('group_footer').send_keys(group.footer)
        # submit group edit
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        """
        Метод удаление первой в списке группы.
        Открываем страницу со списком групп. Находим и удаляем первую
        группу в списке. Возвращаемся к списку групп.
        """
        wd = self.app.wd
        self.open_groups()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit and deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def selected_first_group(self):
        """Внутренний метод селект первой группы в списке"""
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_date):
        """
        Метод изменения одного параметра выбранной группы.
        Открываем страницу со списком групп. Находим и изменяем
        указанный параметр выбранной группы. Возвращаемся к списку групп.
        """
        wd = self.app.wd
        self.open_groups()
        self.selected_first_group()
        # open modification form group
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_date)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        """Метод. Переход на страницу со списком групп."""
        wd = self.app.wd
        wd.find_element_by_link_text('group page').click()