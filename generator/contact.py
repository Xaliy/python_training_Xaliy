# генератор групп - создаем тестовые наборы в формате JSON
import json
import os.path
import random
import string
import getopt
import sys

from model.models import Contact

# из документации import getopt, sys
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:",
                               ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# указываем дефолтные значения
n = 5
f = 'data/contact.json'

# внешнее уравление генератором, иначе по дефолту
for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', f)
with open(file, 'w') as out:
    # dumps() - данные в строку
    out.write(json.dumps(testdate, default=lambda x: x.__dict__, indent=2))