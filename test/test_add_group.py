# -*- coding: utf-8 -*-
from model.models import Group


def test_add_group(app):
    """
    Создаем новую группу.
    Заполняем поля формы и сохраняем.
    """
    app.group.create(Group(name='new_group',
                            header='хедер Группы',
                            footer='футтер группы'))


def test_add_empty_group(app):
    """
    Создаем новую группу с нулевыми параметрами.
    Заполняем поля формы и сохраняем.
    """
    app.group.create(Group(name="",
                           header="",
                           footer=""))
