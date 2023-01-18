# -*- coding: utf-8 -*-
from model.models import Group


def test_modify_group_name(app):
    """
    Частичная модификация параметров группы.
    Изменяем параметр name.
    """
    app.session.login(username='admin', password='secret')
    app.group.modify_first_group(Group(name='Modify name'))
    app.session.logaut_website()


def test_modify_group_header(app):
    """
    Частичная модификация параметров группы.
    Изменяем параметр header.
    """
    app.session.login(username='admin', password='secret')
    app.group.modify_first_group(Group(header='Modify header'))
    app.session.logaut_website()
