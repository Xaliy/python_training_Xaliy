# -*- coding: utf-8 -*-
from model.models import Contact


def test_delete_first_contact(app):
    """Тест удаляем первый контакт в списке."""
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(Contact(firstname='firstname_delete',
                                               middlename='firstname_delete'))
    app.contact.delete_first_contact()
