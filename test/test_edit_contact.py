# -*- coding: utf-8 -*-
from model.models import Contact


def test_edit_first_contact(app):
	"""Тест редактируем первый контакт в списке."""
	app.session.login(username='admin', password='secret')
	app.contact.edit_first_contact(Contact(firstname='ed_firstname-au',
									middlename='ed_middlename-au',
									lastname='ed_lastname-au',
									nickname='ed_nickname-au',
									title='ed_title-au',
									company='ed_company-au',
									address='ed_address-au',
									phone_home='1000-777-8888',
									phone_mobile='1000-333-4444',
									phone_work='10001234',
									fax='1000123456',
									email='ed_gg@mail.cc',
									email2='ed_gg1@mail.cc',
									email3='ed_qq2@mail.cc',
									homepage='www.ed_homepage.cc',
									bday='24',
									bmonth='February',
									byear='2021',
									aday='12',
									amonth='January',
									ayear='2022',
									address2='ed_my address',
									phone2='10000',
									notes='ed_my notes'))
	app.session.logaut_website()