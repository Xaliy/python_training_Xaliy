# -*- coding: utf-8 -*-
import pytest
import random
import string

from model.models import Group

def _random_sting(prefix, maxlen):
    """Подготовка тестовых данных"""
    # генерится строка разных произвольной длины не более maxlen
    # из разных символов
    symbol = string.ascii_letters + string.digits + string.punctuation + ' '*10
    return prefix + ''.join([random.choice(symbol)
                            for i in range(random.randrange(maxlen))])


# 1 вариант с параметрами список с пустыми строками и 5 вариантов с генерацией
testdate = [Group(name="", header="", footer="")] + [
            Group(name=_random_sting('name', 10),
                  header=_random_sting('header', 20),
                  footer=_random_sting('footer', 20)) for i in range(5)
            ]


@pytest.mark.parametrize("group", testdate, ids=[repr(x) for x in testdate])
def test_add_group(app, group):
    """
    Создаем новую группу.
    Заполняем поля формы и сохраняем.
    """
    # сохранить старый список и сравнить с новым списком
    old_groups = app.group.get_group_list()
    # group = Group(name='new_group',
    #     #                         header='хедер Группы',
    #     #                         footer='футтер группы')
    app.group.create(group)
    # сравнение
    # new_groups = app.group.get_group_list()
    # assert len(old_groups)+1 == len(new_groups)
    # сравнение через хеширование
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert (sorted(old_groups, key=Group.if_or_max)
            == sorted(new_groups, key=Group.if_or_max))

# 2 вариант параметризации
# testdate = [
#             Group(name=name, header=header, footer=footer)
#             for name in ['', _random_sting('name', 10)]
#             for header in ['', _random_sting('header', 10)]
#             for footer in ['', _random_sting('footer', 10)]
# ]
