# -*- coding: utf-8 -*-
from random import randrange

from model.models import Group


def test_modify_group_name(app):
    """
    Частичная модификация параметров группы.
    Изменяем параметр name.
    """
    if app.group.count() == 0:
        app.group.create(Group(name='Test_for_modify'))

    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='Modify name')
    # group.id = old_groups[0].id
    group.id = old_groups[index].id
    # app.group.modify_first_group(group)
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    # сравнение
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert (sorted(old_groups, key=Group.if_or_max) ==
            sorted(new_groups, key=Group.if_or_max))

#
# def test_modify_group_header(app):
#     """
#     Частичная модификация параметров группы.
#     Изменяем параметр header.
#     """
#     if app.group.count() == 0:
#         app.group.create(Group(name='Name_for_modify',
#                                header='header_for_modify'))
#
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header='Modify header'))
#     new_groups = app.group.get_group_list()
#     # сравнение
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_group_all(app):
#     """Модификация группы - все поля."""
#     if app.group.count() == 0:
#         app.group.create(Group(name='Name_for_modify',
#                                header='header_for_modify',
#                                footer='header'
#                                ))
#
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(name='edit_group',
#                                        header='edit хедер Группы',
#                                        footer='футтер группы'))
#     new_groups = app.group.get_group_list()
#     # сравнение
#     assert len(old_groups) == len(new_groups)
