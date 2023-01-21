class ContactHelper:
    """фикстуры объекта контакт."""

    def __init__(self, app):
        self.app = app

    def open_form_new_contact(self):
        """Открываем форму для моздания нового контакта."""
        wd = self.app.wd
        wd.find_element_by_link_text('add new').click()

    def return_to_home_page(self):
        """Переходим домашную страницу со списком контактов."""
        wd = self.app.wd
        wd.find_element_by_link_text('home').click()

    def selected_first_contact(self):
        """Внутренний метод селект первого контакта в списке"""
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def _change_field_value(self, field_name, text):
        """Внутренний метод. Выбор и заполнение указанного поля."""
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def _change_field_value_calendar(self, field_name, text):
        """Внутренний метод. Выбор и заполнение календаря."""
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_xpath('//select[@name="' + field_name +
                                     '"]//option[@value="'
                                     + text + '"]').click()

    def _fill_contact_form(self, contact):
        """Внутренний метод заполнения полей формы группа."""
        wd = self.app.wd
        # field
        self._change_field_value('firstname', contact.firstname)
        self._change_field_value('middlename', contact.middlename)
        self._change_field_value('lastname', contact.lastname)
        self._change_field_value('nickname', contact.nickname)
        self._change_field_value('title', contact.title)
        self._change_field_value('company', contact.company)
        self._change_field_value('address', contact.address)
        self._change_field_value('home', contact.phone_home)
        self._change_field_value('mobile', contact.phone_mobile)
        self._change_field_value('work', contact.phone_work)
        self._change_field_value('fax', contact.fax)
        self._change_field_value('email', contact.email)
        self._change_field_value('email2', contact.email2)
        self._change_field_value('email3', contact.email3)
        self._change_field_value('homepage', contact.homepage)
        # calendars
        self._change_field_value_calendar('bday', contact.bday)
        self._change_field_value_calendar("bmonth", contact.bmonth)
        self._change_field_value('byear', contact.byear)
        self._change_field_value_calendar('aday', contact.aday)
        self._change_field_value_calendar('amonth', contact.amonth)
        self._change_field_value('ayear', contact.ayear)
        # next field
        self._change_field_value('address2', contact.address2)
        self._change_field_value('phone2', contact.phone2)
        self._change_field_value('notes', contact.notes)

    def create_new_contact(self, contact):
        """
        Вызов метода открытия формы создания нового контакта.
        Добавляем новый контакт.
        Заполняем поля формы и сохраняем.
        Вызов метода перехода на домашную страницу.
        """
        wd = self.app.wd
        self.open_form_new_contact()
        # text fields
        self._fill_contact_form(contact)
        # save
        wd.find_element_by_xpath(
                '//div[@id="content"]/form/input[21]').click()
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        """
        Вызов метода открытия формы создания нового контакта.
        Добавляем новый контакт.
        Заполняем поля формы и сохраняем.
        Вызов метода перехода на домашную страницу.
        """
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        self.selected_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # modify fill
        self._fill_contact_form(contact)
        # save
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        """
        Метод удаление первого в списке контакта.
        Открываем домашную страницу со списком контактов.
        Отмечаем первый контакт в списке. Удаляем.
        """
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        self.selected_first_contact()
        # submit and deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # модальное окно
        wd.switch_to.alert.accept()
        self.return_to_home_page()
