# -*- coding: utf-8 -*-
import pytest

from application import Application
from models import Contact


@pytest.fixture
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture

	
def test_add_contact(app):
	"""
	Создаем нНовый контакт.
	Заполняем поля формы и сохраняем.
	"""
	app.login(username='admin', password='secret')
	app.create_new_contact(Contact(firstname='firstname-au',
									middlename='middlename-au',
									lastname='lastname-au',
									nickname='nickname-au',
									title='title-au',
									company='company-au',
									address='address-au',
									phone_home='999-777-8888',
									phone_mobile='777-333-4444',
									phone_work='1234',
									fax='123456',
									email='gg@mail.cc',
									email2='gg1@mail.cc',
									email3='qq2@mail.cc',
									homepage='www.homepage.cc',
									bday='4',
									bmonth='April',
									byear='2000',
									aday='2',
									amonth='February',
									ayear='2023',
									address2='my address',
									phone2='10',
									notes='my notes'))
	app.logaut_website()
