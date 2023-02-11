# -*- coding: utf-8 -*-
# генерация тестовых данных - вынесли в отдельный файл
from model.models import Group


# для отладки фиксированный набор
testdata = [
    Group(name='new_group1', header='хедер Группы1', footer='футтер группы1'),
    Group(name='new_group2', header='хедер Группы2', footer='футтер группы2')
]
