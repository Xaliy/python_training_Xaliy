# -*- coding: utf-8 -*-

def test_delete_first_contact(app):
    """Тест удаляем первый контакт в списке."""
    app.contact.delete_first_contact()
