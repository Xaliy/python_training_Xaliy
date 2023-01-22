# -*- coding: utf-8 -*-
from model.models import Group


def test_delete_first_group(app):
    """Тест удаляем первую группу в списке."""
    # проверка на наличие хотя бы одной группы
    if app.group.count() == 0:
        app.group.create(Group(name="Test_delete"))
    app.group.delete_first_group()
