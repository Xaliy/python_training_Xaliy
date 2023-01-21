# -*- coding: utf-8 -*-

def test_delete_first_group(app):
    """Тест удаляем первую группу в списке."""
    app.group.delete_first_group()
