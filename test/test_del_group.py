# -*- coding: utf-8 -*-
import random

from model.models import Group


def test_delete_some_group(app, db, check_ui):
    """Тест удаляем произвольную группу в списке. Через БД."""
    # проверка на наличие хотя бы одной группы
    if len(db.get_group_list_db()) == 0:
        app.group.create(Group(name='Test_delete'))
    old_groups = sorted(db.get_group_list_db(), key=Group.if_or_max)
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = sorted(db.get_group_list_db(), key=Group.if_or_max)
    # сравнение
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups

    if check_ui:
        for i in new_groups:
            for k in app.group.get_group_list():
                if k.id == i.id:
                    assert (k == i)

# def test_delete_some_group(app):
#     """
#     Тест удаляем произвольную группу в списке.
#     Сравнение через интерфейс.
#     """
#     if app.group.count() == 0:
#         app.group.create(Group(name="Test_delete"))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     app.group.delete_group_by_index(index)
#     new_groups = app.group.get_group_list()
#     # сравнение
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[index:index+1] = []
#     assert old_groups == new_groups
#
# def test_delete_first_group(app):
#     """Тест удаляем первую  группу в списке."""
#     # проверка на наличие хотя бы одной группы
#     if app.group.count() == 0:
#         app.group.create(Group(name="Test_delete"))
#     old_groups = app.group.get_group_list()
#     app.group.delete_first_group()
#     new_groups = app.group.get_group_list()
#     # сравнение
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[0:1] = []
#     assert old_groups == new_groups
