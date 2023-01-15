# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.models import Group


@pytest.fixture
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture


def test_add_group(app):
	"""
	Создаем новую группу.
	Заполняем поля формы и сохраняем.
	"""
	app.login(username='admin', password='secret')
	app.create_group(Group(name='new_group',
						   header='хедер Группы',
						   footer='футтер группы'))
	app.logaut_website()


def test_add_empty_group(app):
	"""
	Создаем новую группу с нулевыми параметрами.
	Заполняем поля формы и сохраняем.
	"""
	app.login(username="admin", password="secret")
	app.create_group(Group(name="",
						   header="",
						   footer=""))
	app.logaut_website()
