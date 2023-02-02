# -*- coding: utf-8 -*-
from model.models import Group


def test_add_group(app):
    """
    Создаем новую группу.
    Заполняем поля формы и сохраняем.
    """
    # сохранить старый список и сравнить с новым списком
    old_groups = app.group.get_group_list()
    app.group.create(Group(name='new_group',
                            header='хедер Группы',
                            footer='футтер группы'))
    new_groups = app.group.get_group_list()
    # сравнение
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    """
    Создаем новую группу с нулевыми параметрами.
    Заполняем поля формы и сохраняем.
    """
    # сохранить старый список и сравнить с новым списком
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="",
                           header="",
                           footer=""))
    new_groups = app.group.get_group_list()
    # сравнение
    assert len(old_groups) + 1 == len(new_groups)
