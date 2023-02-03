# -*- coding: utf-8 -*-
from model.models import Contact


def test_edit_first_contact(app):
    """Тест редактируем первый контакт в списке."""
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(Contact(firstname='firstname_for_edit',
                                       middlename='firstname_for_edit'))
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname='ed_firstname-au',
                                   middlename='ed_middlename-au',
                                   lastname='ed_lastname-au',
                                   nickname='ed_nickname-au',
                                   title='ed_title-au',
                                   company='ed_company-au',
                                   address='ed_address-au',
                                   phone_home='1000-777-8888',
                                   phone_mobile='1000-333-4444',
                                   phone_work='10001234',
                                   fax='1000123456',
                                   email='ed_gg@mail.cc',
                                   email2='ed_gg1@mail.cc',
                                   email3='ed_qq2@mail.cc',
                                   homepage='www.ed_homepage.cc',
                                   bday='24',
                                   bmonth='October',
                                   byear='2091',
                                   aday='15',
                                   amonth='april',
                                   ayear='2020',
                                   address2='ed_my address',
                                   phone2='10000',
                                   notes='ed_my notes')

    contact.id = old_contact[0].id
    app.contact.edit_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    # сравнение
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert (sorted(old_contact, key=Contact.if_or_max)
            == sorted(new_contact, key=Contact.if_or_max))
