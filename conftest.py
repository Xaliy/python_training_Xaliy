# -*- coding: utf-8 -*-
import os.path
import json

import pytest

from fixture.application import Application


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    if target is None:
        # config_file = (прикрепляем  join(определяем
        # директорию(преобразовали путь текущего __file__
        # в абсолютный)), и то что приклеиваем) - т.о нашли путь к target.json
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   request.config.getoption('--target'))
        # with open(request.config.getoption('--target')) as conf:
        with open(config_file) as conf:
            target = json.load(conf)
        # base_url = request.config.getoption('--baseUrl')
        # username = request.config.getoption('--username')
        # password = request.config.getoption('--password')
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])

    fixture.session.ensure_login(username=target['username'],
                                 password=target['password'])
    return fixture


# autouse=True - автом. использование метода
@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logaut()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


# добавление дополнительных параметров
# в данном случае ввод значения из консоли
def pytest_addoption(parser):
    """функция добавления опции командной строки"""
    parser.addoption("--browser", action="store", default='firefox')
    parser.addoption("--target", action="store",
                     default='target.json')
    # это уже не нужно- берем из одного файла
    # parser.addoption("--target", action="store", default='target.json')
    # parser.addoption("--target", action="store", default='target.json')
