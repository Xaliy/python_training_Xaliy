# -*- coding: utf-8 -*-
from model.models import Contact


def test_add_contact(app):
    """
    Создаем новый контакт.
    Заполняем поля формы и сохраняем.
    """
    # сохранить старый список и сравнить с новым списком
    old_contact = app.contact.get_contact_list()
    contract = Contact(firstname='firstname-au',
                                   middlename='middlename-au',
                                   lastname='lastname-au',
                                   nickname='nickname-au',
                                   title='title-au',
                                   company='company-au',
                                   address='address-au',
                                   phone_home='9997778888',
                                   phone_mobile='7773334444',
                                   phone_work='123499',
                                   fax='123456',
                                   email='gg@mail.cc',
                                   email2='gg1@mail.cc',
                                   email3='qq2@mail.cc',
                                   homepage='www.homepage.cc',
                                   bday="4",
                                   bmonth='April',
                                   byear='2000',
                                   aday="2",
                                   amonth='March',
                                   ayear='2023',
                                   address2='my address',
                                   phone2='10789464',
                                   notes='my notes')

    app.contact.create_new_contact(contract)
    # new_contact = app.contact.get_contact_list()
    # сравнение
    assert len(old_contact) + 1 == app.contact.count_contact()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contract)
    assert (sorted(old_contact, key=Contact.if_or_max)
            == sorted(new_contact, key=Contact.if_or_max))
