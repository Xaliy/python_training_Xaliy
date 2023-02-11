# -*- coding: utf-8 -*-
# генерация тестовых данных - вынесли в отдельный файл
import random
import string

from model.models import Group


# для отладки фиксированный набор
constant = [
    Group(name='new_group1', header='хедер Группы1', footer='футтер группы1'),
    Group(name='new_group2', header='хедер Группы2',footer='футтер группы2'),
]


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
