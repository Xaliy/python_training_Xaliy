# -*- coding: utf-8 -*-
from model.models import Contact

def test_add_contact(app, db, json_contacts, check_ui):
    """
    Создаем новый контакт.
    Заполняем поля формы и сохраняем. используем JSON и DB.
    """
    # сохранить старый список и сравнить с новым списком
    contact = json_contacts
    old_contact = db.get_contact_list_db()
    print(old_contact)

    app.contact.create_new_contact(contact)
    # new_contact = app.contact.get_contact_list()
    # сравнение для json не валидно
    # assert len(old_contact) + 1 == app.contact.count_contact()
    new_contacts = db.get_contact_list_db()
    old_contact.append(contact)
    assert (sorted(old_contact, key=Contact.if_or_max)
            == sorted(new_contacts, key=Contact.if_or_max))
    if check_ui:
        for i in new_contacts:
            for k in app.contact.get_contact_list():
                if i.id == k.id:
                    assert (k == i)




# def test_add_contact(app, json_contacts):
#     """
#     Создаем новый контакт.
#     Заполняем поля формы и сохраняем. используем JSON.
#     """
#     # сохранить старый список и сравнить с новым списком
#     contact = json_contacts
#     old_contact = app.contact.get_contact_list()
#     app.contact.create_new_contact(contact)
#     # new_contact = app.contact.get_contact_list()
#     # сравнение
#     assert len(old_contact) + 1 == app.contact.count_contact()
#     new_contact = app.contact.get_contact_list()
#     old_contact.append(contact)
#     assert (sorted(old_contact, key=Contact.if_or_max)
#             == sorted(new_contact, key=Contact.if_or_max))
