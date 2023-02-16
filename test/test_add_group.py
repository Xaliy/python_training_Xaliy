# -*- coding: utf-8 -*-
from model.models import Group


def test_add_group(app, db, json_groups, check_ui):
    """
    Создаем новую группу.
    Заполняем поля формы и сохраняем.
    """
    # сохранить старый список и сравнить с новым списком
    group = json_groups
    old_groups = db.get_group_list_db()  # загрузка из базы
    app.group.create(group)
    # сравнение
    # для работы с БД  в fixture/db.py autocommit=True
    new_groups = db.get_group_list_db()  # загрузка из БД
    old_groups.append(group)
    assert (sorted(old_groups, key=Group.if_or_max)
            == sorted(new_groups, key=Group.if_or_max))
    if True:
    # if check_ui:
        for i in new_groups:
            for k in app.group.get_group_list():
                if i.id == k.id:
                    assert (k == i)





    # # для интерфейса
    # group = json_groups
    # old_groups = app.group.get_group_list()
    # app.group.create(group)
    # # сравнение
    # # сравнение через хеширование
    # assert len(old_groups) + 1 == app.group.count()
    # new_groups = app.group.get_group_list()
    # old_groups.append(group)
    # assert (sorted(old_groups, key=Group.if_or_max)
    #         == sorted(new_groups, key=Group.if_or_max))
