# -*- coding: utf-8 -*-
# from random import randrange
import random

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

    contact_new_edit = Contact(firstname='ed_firstname-au',
                                   lastname='ed_lastname-au',
                                   address='ed_address-au'
                                   )
    old_contacts = sorted(db.get_contact_list_db(), key=Contact.if_or_max)
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact.id, contact_new_edit)
    new_contacts = sorted(db.get_contact_list_db(), key=Contact.if_or_max)
    # сравнение
    assert len(old_contacts) == len(new_contacts)

    for indx, i in enumerate(new_contacts):
        if i.id == contact.id:
            assert (
                i.firstname == contact_new_edit.firstname and
                i.lastname == contact_new_edit.lastname and
                i.address == contact_new_edit.address
            )
        if check_ui:
            for k in app.contact.get_contact_list():
                if k.id == i.id:
                    assert (k == i)



# def test_edit_first_contact(app):
#     """Тест редактируем рандомный контакт в списке."""
#     if app.contact.count_contact() == 0:
#         app.contact.create_new_contact(Contact(firstname='firstname_for_edit',
#                                        middlename='firstname_for_edit'))
#     old_contact = app.contact.get_contact_list()
#     index = randrange(len(old_contact))
#     contact = Contact(firstname='ed_firstname-au',
#                                    middlename='ed_middlename-au',
#                                    lastname='ed_lastname-au',
#                                    nickname='ed_nickname-au',
#                                    title='ed_title-au',
#                                    company='ed_company-au',
#                                    address='ed_address-au',
#                                    phone_home='10007778888',
#                                    phone_mobile='10003334444',
#                                    phone_work='10001234',
#                                    fax='1000123456',
#                                    email='edgg@mail.cc',
#                                    email2='edgg1@mail.cc',
#                                    email3='edqq2@mail.cc',
#                                    homepage='www.edhomepage.cc',
#                                    bday='24',
#                                    bmonth='October',
#                                    byear='2091',
#                                    aday='15',
#                                    amonth='april',
#                                    ayear='2020',
#                                    address2='ed_my address',
#                                    phone2='100008797',
#                                    notes='ed_my notes')
#
#     contact.id = old_contact[index].id
#     app.contact.edit_contact_by_index(index, contact)
#     new_contact = app.contact.get_contact_list()
#     # сравнение
#     assert len(old_contact) == len(new_contact)
#     old_contact[index] = contact
#     assert (sorted(old_contact, key=Contact.if_or_max)
#             == sorted(new_contact, key=Contact.if_or_max))


# def test_edit_first_contact(app):
#     """Тест редактируем первый контакт в списке."""
#     if app.contact.count_contact() == 0:
#         app.contact.create_new_contact(Contact(firstname='firstname_for_edit',
#                                        middlename='firstname_for_edit'))
#     old_contact = app.contact.get_contact_list()
#     index = randrange(len(old_contact))
#     contact = Contact(firstname='ed_firstname-au',
#                                    middlename='ed_middlename-au',
#                                    lastname='ed_lastname-au',
#                                    nickname='ed_nickname-au',
#                                    title='ed_title-au',
#                                    company='ed_company-au',
#                                    address='ed_address-au',
#                                    phone_home='1000-777-8888',
#                                    phone_mobile='1000-333-4444',
#                                    phone_work='10001234',
#                                    fax='1000123456',
#                                    email='ed_gg@mail.cc',
#                                    email2='ed_gg1@mail.cc',
#                                    email3='ed_qq2@mail.cc',
#                                    homepage='www.ed_homepage.cc',
#                                    bday='24',
#                                    bmonth='October',
#                                    byear='2091',
#                                    aday='15',
#                                    amonth='april',
#                                    ayear='2020',
#                                    address2='ed_my address',
#                                    phone2='10000',
#                                    notes='ed_my notes')
#
#     contact.id = old_contact[index].id
#     app.contact.edit_contact_by_index(index, contact)
#     new_contact = app.contact.get_contact_list()
#     # сравнение
#     assert len(old_contact) == len(new_contact)
#     old_contact[index] = contact
#     assert (sorted(old_contact, key=Contact.if_or_max)
#             == sorted(new_contact, key=Contact.if_or_max))
