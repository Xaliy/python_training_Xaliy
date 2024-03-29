# -*- coding: utf-8 -*-
import re

from model.models import Contact


class ContactHelper:
    """фикстуры объекта контакт."""

    def __init__(self, app):
        self.app = app

    def open_form_new_contact(self):
        """Открываем форму для создания нового контакта."""
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and
                len(wd.find_elements_by_xpath(
                '//div[@id="content"]/form/input[21]')) > 0):
            wd.find_element_by_link_text('add new').click()

    def return_to_home_page(self):
        """Переходим домашную страницу со списком контактов."""
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and
                len(wd.find_elements_by_xpath("//input[@value='Delete']")) > 0):
            wd.find_element_by_link_text('home').click()

    def selected_first_contact(self):
        """Внутренний метод селект первого контакта в списке."""
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def _selected_contact_by_index(self, index):
        """Внутренний метод селект контакта в списке по индексу."""
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def _selected_contact_by_id(self, id):
        """Внутренний метод селект контакта в списке по ID."""
        wd = self.app.wd
        wd.find_element_by_id(f"{id}").click()
        # wd.find_element_by_css_selector(f"#{id}]").click()
        # wd.find_element_by_xpath(f"//input[@id='{id}']").click()

    def count_contact(self):
        """Метод определяет наличие контактов в списке. Count."""
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

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
            # wd.find_element_by_xpath('//select[@name="' + field_name +
            #                          '"]//option[@value="'
            #                          + text + '"]').click()
            wd.find_element_by_xpath(
                f'''//select[@name="{field_name}"]
                    //option[@value="{text}"]''').click()

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
        self.contact_cache = None

    def edit_first_contact(self, contact):
        """Метод редактирования первого контакта в списке."""
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        """Метод редактирования указанного контакта в списке."""
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        self._selected_contact_by_index(index)
        tr = str(index + 2)
        # wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # wd.find_element_by_xpath('//table[@id="maintable"]/tbody/tr['
        #                          + tr + ']/td[8]/a/img').click()
        # wd.find_element_by_xpath('//tr[' + tr + ']/td[8]/a/img').click()
        wd.find_element_by_xpath(f'//tr[{tr}]/td[8]/a/img').click()
        # modify fill
        self._fill_contact_form(contact)
        # save
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        """Метод редактирования контакта в списке по ID."""
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        self._selected_contact_by_id(id)
        wd.find_element_by_css_selector(
                f".center a[href='edit.php?id={id}']").click()
        # modify fill
        self._fill_contact_form(contact)
        # save
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        """Метод удаление первого контакта в списке."""
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        """
        Метод удаление контакта в списке по индексу.
        Открываем домашную страницу со списком контактов.
        Отмечаем нужный контакт в списке. Удаляем.
        """
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        self._selected_contact_by_index(index)
        # submit and deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # модальное окно
        wd.switch_to.alert.accept()
        # проверка на удаление
        wd.find_element_by_css_selector("div.msgbox")
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        """
        Метод удаление контакта в списке по ID.
        Открываем домашную страницу со списком контактов.
        Отмечаем нужный контакт в списке. Удаляем.
        """
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        self._selected_contact_by_id(id)
        # submit and deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # модальное окно
        wd.switch_to.alert.accept()
        # проверка на удаление
        wd.find_element_by_css_selector("div.msgbox")
        self.return_to_home_page()
        self.contact_cache = None

    # кэширование данных
    contact_cache = None

    def get_contact_list(self):
        """Метод сравнение списков контактов."""
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []

            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_css_selector("td")
                lastname = cells[1].text
                firstname = cells[2].text
                addr = cells[3].text
                all_email = cells[4].text
                # email = cells[5].text
                # email = cells[4].text
                all_phones = cells[5].text
                id = element.find_element_by_name(
                        "selected[]").get_attribute("value")
                # id = cells[0].find_element_by_tag_name(
                #  "input").get_attribute("value")  # вариант локатора
                # all_phones = cells[5].text.splitlines()
                # self.contact_cache.append(Contact(lastname=lastname,
                #                                   firstname=firstname, id=id,
                #                                   phone_home=all_phones[0],
                #                                   phone_mobile=all_phones[1],
                #                                   phone_work=all_phones[2],
                #                                   phone2=all_phones[3]
                # )
                self.contact_cache.append(
                        Contact(
                            id=id, lastname=lastname, firstname=firstname,
                            all_gmail_from_home_page=all_email,
                            address=addr,
                            all_phones_from_home_page=all_phones)
                )

        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        """Открыть страницу контакта на редактирование по индексу."""
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        """Открыть страницу контакта на просмотр по индексу."""
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        """Вернуть информацию с формы редактирования контакта."""
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute(
            "value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       phone_home=phone_home, phone_mobile=phone_mobile,
                       phone_work=phone_work, phone2=phone2, address=address,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        """Вернуть информацию с формы просмотра контакта."""
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text

        if text is not '':
            phone_home = re.search("H: (.*)", text).group(1)
            phone_work = re.search("W: (.*)", text).group(1)
            phone_mobile = re.search("M: (.*)", text).group(1)
            phone2 = re.search("P: (.*)", text).group(1)
            return Contact(phone_home=phone_home, phone_mobile=phone_mobile,
                           phone_work=phone_work, phone2=phone2)
        return Contact(phone_home='', phone_mobile='',
                       phone_work='', phone2='')

    def get_contact_from_homepage_page(self, index):
        """Вернуть информацию по контакту со страницы списка контактов."""
        wd = self.app.wd
        self.return_to_home_page()
        element = wd.find_elements_by_name("entry")[index]
        cells = element.find_elements_by_tag_name("td")
        id = element.find_element_by_name("selected[]").get_attribute("value")
        firstname = cells[2].text
        lastname = cells[1].text
        address = cells[3].text
        email = cells[4].text
        all_phones = cells[5].text
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       email=email, address=address,
                       all_phones_from_home_page=all_phones,
                       all_gmail_from_home_page=email)
