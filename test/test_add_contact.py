# -*- coding: utf-8 -*-
from model.models import Contact


def test_add_contact(app, data_contract):
    """
    Создаем новый контакт.
    Заполняем поля формы и сохраняем.
    """
    # сохранить старый список и сравнить с новым списком
    contract = data_contract
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contract)
    # new_contact = app.contact.get_contact_list()
    # сравнение
    assert len(old_contact) + 1 == app.contact.count_contact()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contract)
    assert (sorted(old_contact, key=Contact.if_or_max)
            == sorted(new_contact, key=Contact.if_or_max))
