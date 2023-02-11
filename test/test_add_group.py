# -*- coding: utf-8 -*-
from model.models import Group


def test_add_group(app, data_groups):
    """
    Создаем новую группу.
    Заполняем поля формы и сохраняем.
    """
    # сохранить старый список и сравнить с новым списком
    group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # сравнение
    # сравнение через хеширование
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert (sorted(old_groups, key=Group.if_or_max)
            == sorted(new_groups, key=Group.if_or_max))
