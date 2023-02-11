# -*- coding: utf-8 -*-
from model.models import Contact


# для отладки фиксированный набор
# constant \
testdata = [
    Contact(firstname='firstname-au1', middlename='middlename-au1',
            lastname='lastname-au1', nickname='nickname-au1',
            title='title-au1', company='company-au1',
            address='address-au1', phone_home='1117778888',
            phone_mobile='111114444', phone_work='11111234',
            fax='111456', email='gg1@mail.cc', email2='gg12@mail.cc',
            email3='qq13@mail.cc', homepage='www.homepage1.cc',
            bday="4", bmonth='April', byear='2000', aday="2",
            amonth='March', ayear='2023', address2='myaddress1',
            phone2='1111222222', notes='mynotes1'),
    Contact(firstname='firstname-au2', middlename='middlename-au2',
            lastname='lastname-au2', nickname='nickname-au2',
            title='title-au2', company='company-au2',
            address='address-au2', phone_home='22227778888',
            phone_mobile='22224444', phone_work='11111234',
            fax='222456', email='gg2@mail.cc', email2='gg22@mail.cc',
            email3='qq23@mail.cc', homepage='www.homepage2.cc',
            bday="14", bmonth='April', byear='2001', aday="2",
            amonth='March', ayear='2022', address2='myaddress2',
            phone2='2222222222', notes='mynotes2')
    ]
