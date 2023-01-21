# -*- coding: utf-8 -*-
from model.models import Group


def test_modify_group_name(app):
    """
    Частичная модификация параметров группы.
    Изменяем параметр name.
    """
    app.group.modify_first_group(Group(name='Modify name'))


def test_modify_group_header(app):
    """
    Частичная модификация параметров группы.
    Изменяем параметр header.
    """
    app.group.modify_first_group(Group(header='Modify header'))


def test_modify_group_all(app):
    """
    Создаем новую группу.
    Заполняем поля формы и сохраняем.
    """
    app.group.modify_first_group(Group(name='edit_group',
                           header='edit хедер Группы',
                           footer='edit футтер группы'))
