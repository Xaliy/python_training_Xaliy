# генератор групп - создаем тестовые наборы в формате JSON
import json
import os.path
import random
import string
import getopt
import sys

from model.models import Group

# из документации import getopt, sys
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:",
                               ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# указываем дефолтные значения
n = 5
f = 'data/groups.json'

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
    symbol = string.ascii_letters+string.digits+string.punctuation+' '*10
    return prefix+''.join(
            [random.choice(symbol) for i in range(random.randrange(maxlen))])


# 1 вариант с параметрами список с пустыми строками и 5 вариантов с генерацией
testdate = [Group(name='', header='', footer='')]+[
    Group(name=_random_sting('name', 10), header=_random_sting('header', 20),
          footer=_random_sting('footer', 20)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', f)
with open(file, 'w') as out:
    # dumps() - данные в строку
    out.write(json.dumps(testdate, default=lambda x: x.__dict__, indent=2))
