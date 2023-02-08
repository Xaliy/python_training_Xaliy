# -*- coding: utf-8 -*-
import pytest
import random
import string


from model.models import Contact


def _random_sting(prefix, maxlen):
    """Подготовка тестовых данных"""
    # генерится строка разных произвольной длины не более maxlen
    # из разных символов
    # symbol = string.ascii_letters + string.digits +
    # string.punctuation + ' '*10
    symbol = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbol)
                            for i in range(random.randrange(maxlen))])


def _random_phone():
    """Подготовка тестовых телефонов по упрощенной схеме"""
    # генерится строка разных произвольной длины не более maxlen
    # из разных символов
    symbol = string.digits
    return ''.join([random.choice(symbol)
                    for i in range(random.randrange(12))])


def _random_email(prefix):
    """Подготовка тестовых email по упрощенной схеме"""
    # генерится строка разных произвольной длины не более maxlen
    # из разных символов
    symbol = string.ascii_letters + string.digits
    return prefix + '@'.join([''.join([random.choice(symbol)
                              for i in range(random.randrange(2, 4))]),
                              ''.join([random.choice(symbol) for i in
                                       range(random.randrange(3, 7))])])


# параметризованны список
testdate = [Contact(firstname="", middlename="", lastname="")] + [
             Contact(firstname=_random_sting('firstname', 10),
                     middlename=_random_sting('middlename', 10),
                     lastname=_random_sting('lastname', 10),
                     nickname=_random_sting('nickname', 10),
                     title=_random_sting('title', 20),
                     company=_random_sting('company', 10),
                     address=_random_sting('address', 10),
                     phone_home=_random_phone(),
                     phone_mobile=_random_phone(),
                     phone_work=_random_phone(),
                     fax=_random_phone(),
                     email=_random_email('email'),
                     email2=_random_email('email2'),
                     email3=_random_email('email3'),
                     homepage='www.homepage.cc',
                     bday=str(random.randrange(30)),
                     bmonth='April',
                     byear=str(random.randrange(1970, 2023)),
                     aday=str(random.randrange(30)),
                     amonth='March',
                     ayear=str(random.randrange(1970, 2023)),
                     address2=_random_sting('address2', 20),
                     phone2=_random_phone(),
                     notes=_random_sting('notes', 10))
             for i in range(5)
            ]


@pytest.mark.parametrize("contract", testdate, ids=[repr(x) for x in testdate])
def test_add_contact(app, contract):
    """
    Создаем новый контакт.
    Заполняем поля формы и сохраняем.
    """

    # сохранить старый список и сравнить с новым списком
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contract)
    # new_contact = app.contact.get_contact_list()
    # сравнение
    assert len(old_contact) + 1 == app.contact.count_contact()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contract)
    assert (sorted(old_contact, key=Contact.if_or_max)
            == sorted(new_contact, key=Contact.if_or_max))
