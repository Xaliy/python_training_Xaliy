# -*- coding: utf-8 -*-
# from random import randrange
import random

from model.models import Contact


def test_delete_contact_by_id(app, db, check_ui):
    """Тест удаляем контакт в списке по ID."""
    # проверяем наличие одного контакта
    # print(len(db.get_contact_list_db()))
    if len(db.get_contact_list_db()) == 0:
        app.contact.create_new_contact(Contact(firstname='firstname_delete',
                                               lastname='lastname_delete'))
    old_contacts = db.get_contact_list_db()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list_db()
    # сравнение списка контактов
    assert len(old_contacts) - 1 == len(new_contacts)
    # проверка на удаленную строку по ID
    for i in new_contacts:
        assert contact.id != i.id

    if check_ui:
        for k in app.contact.get_contact_list():
            assert contact.id != k.id
#
# def test_delete_contact_by_index(app):
#     """Тест удаляем контакт в списке по index."""
#     # проверяем наличие одного контакта
#     if app.contact.count_contact() == 0:
#         app.contact.create_new_contact(Contact(firstname='firstname_delete',
#                                                lastname='lastname_delete'))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     app.contact.delete_contact_by_index(index)
#     new_contacts = app.contact.get_contact_list()
#     # сравнение списка контактов
#     assert len(old_contacts) - 1 == len(new_contacts)
#     old_contacts[index:index+1] = []
#     assert old_contacts == new_contacts


# def test_delete_first_contact(app):
#     """Тест удаляем первый контакт в списке."""
#     # проверяем наличие одного контакта
#     if app.contact.count_contact() == 0:
#         app.contact.create_new_contact(Contact(firstname='firstname_delete',
#                                                lastname='lastname_delete'))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.delete_first_contact()
#     new_contacts = app.contact.get_contact_list()
#     # сравнение списка контактов
#     assert len(old_contacts) - 1 == len(new_contacts)
#     old_contacts[0:1] = []
#     assert old_contacts == new_contacts