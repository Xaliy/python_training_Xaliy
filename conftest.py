# -*- coding: utf-8 -*-
import os.path
import json

import jsonpickle  # pip install jsonpickle
import pytest
import importlib

from fixture.application import Application
from fixture.db import DbFixture


fixture = None
target = None


def load_config(file):
    """Загрузка параметров конекта"""
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(
                                    os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--target'))['web']

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])

    fixture.session.ensure_login(username=web_config['username'],
                                 password=web_config['password'])
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
# в данном случае ввод значения из консоли и из JSON
def pytest_addoption(parser):
    """функция добавления опции командной строки"""
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')
    parser.addoption('--check_ui', action='store_true')


@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'],
                          password=db_config['password'])

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption('--check_ui')


# получить всю информайцию
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x)
                                                         for x in testdata])
        elif fixture.startswith('json_'):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x)
                                                         for x in testdata])


def load_from_module(module):
    """Загрузка тестовых данных из файла"""
    return importlib.import_module(f'data.{module}').testdata


def load_from_json(file):
    """Загрузка тестовых данных из файла в формате JSON"""
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           f'data/{file}.json')) as f:
        return jsonpickle.decode(f.read())
