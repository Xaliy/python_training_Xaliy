# -*- coding: utf-8 -*-
from random import randrange
# import random

from model.models import Contact


def test_edit_contact_db(app, db, check_ui):
    """
    Тест редактируем контакт, найденный по ID.
    Проверка по БД по укороченному сценарию.
    Проверка на функциональность.
    """
    if len(db.get_contact_list_db()) == 0:
        app.contact.create_new_contact(
            Contact(firstname='firstname_edit', lastname='lastname_edit'))

    contact_new_edit = Contact(
                        firstname='ed_firstname-au',
                        lastname='ed_lastname-au',
                        address='ed_address-au'
                       )

    old_contacts = sorted(db.get_contact_list_db(), key=Contact.if_or_max)
    # contact = random.choice(old_contacts)
    index = randrange(len(old_contacts))
    contact_new_edit.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact_new_edit.id, contact_new_edit)
    new_contacts = sorted(db.get_contact_list_db(), key=Contact.if_or_max)
    # сравнение
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact_new_edit
    assert (sorted(old_contacts, key=Contact.if_or_max) ==
            sorted(new_contacts, key=Contact.if_or_max))

    if check_ui:
        assert (sorted(new_contacts, key=Contact.if_or_max) ==
                sorted(app.contact.get_contact_list(), key=Contact.if_or_max))
