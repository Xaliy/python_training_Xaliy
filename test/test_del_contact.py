# -*- coding: utf-8 -*-
from model.models import Contact


def test_delete_first_contact(app):
    """Тест удаляем первый контакт в списке."""
    # проверяем наличие одного контакта
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(Contact(firstname='firstname_delete',
                                               lastname='lastname_delete'))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    # сравнение списка контактов
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
