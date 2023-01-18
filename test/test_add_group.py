# -*- coding: utf-8 -*-
from model.models import Group


def test_add_group(app):
    """
    Создаем новую группу.
    Заполняем поля формы и сохраняем.
    """
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name='new_group',
                            header='хедер Группы',
                            footer='футтер группы'))
    app.session.logaut_website()


def test_add_empty_group(app):
    """
    Создаем новую группу с нулевыми параметрами.
    Заполняем поля формы и сохраняем.
    """
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="",
                           header="",
                           footer=""))
    app.session.logaut_website()
