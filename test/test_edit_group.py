# -*- coding: utf-8 -*-
from model.models import Group


def test_edit_first_group(app):
	"""
	Создаем новую группу.
	Заполняем поля формы и сохраняем.
	"""
	app.session.login(username='admin', password='secret')
	app.group.edit(Group(name='edit_group',
						   header='edit хедер Группы',
						   footer='edit футтер группы'))
	app.session.logaut_website()
