# -*- coding: utf-8 -*-
from random import randrange
import random

from model.models import Group


def test_modify_group_db(app, db, check_ui):
    """
    Частичная модификация параметров группы по ID.
    Изменяем параметр name.
    """
    if len(db.get_group_list_db()) == 0:
        app.group.create(Group(name='Test_for_modify'))

    group_param_new = Group(name='modifay_name_group',
                            # header='modifay_хедер группы'
                            # footer='modifay_футтер группы'
                            )

    old_groups = sorted(db.get_group_list_db(), key=Group.if_or_max)
    # group = random.choice(old_groups)
    index = randrange(len(old_groups))
    group_param_new.id = old_groups[index].id
    app.group.modify_group_by_id(group_param_new.id, group_param_new)
    new_groups = sorted(db.get_group_list_db(), key=Group.if_or_max)
    # сравнение
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group_param_new
    assert (sorted(old_groups, key=Group.if_or_max) ==
            sorted(new_groups, key=Group.if_or_max))

        # if True:
    if check_ui:
        assert sorted(new_groups, key=Group.if_or_max) == sorted(
            app.group.get_group_list(), key=Group.if_or_max)
        # def _clean_gr(group):
        #     return Group(id=group.id, name=group.name.strip())
        #
        # for k in app.group.get_group_list():
        #     if k.id == i.id:
        #         assert (k == _clean_gr(i))

# def test_modify_group_name(app):
    # """
    # Частичная модификация параметров группы по индексу.
    # Изменяем параметр name.
    # """
    # if app.group.count() == 0:
    #     app.group.create(Group(name='Test_for_modify'))
    #
    # old_groups = app.group.get_group_list()
    # index = randrange(len(old_groups))
    # group = Group(name='Modify name')
    # # group.id = old_groups[0].id
    # group.id = old_groups[index].id
    # # app.group.modify_first_group(group)
    # app.group.modify_group_by_index(index, group)
    # new_groups = app.group.get_group_list()
    # # сравнение
    # assert len(old_groups) == len(new_groups)
    # old_groups[index] = group
    # assert (sorted(old_groups, key=Group.if_or_max) ==
    #         sorted(new_groups, key=Group.if_or_max))


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
