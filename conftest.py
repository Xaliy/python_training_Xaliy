# -*- coding: utf-8 -*-
import os.path
import json

import pytest
import importlib

from fixture.application import Application


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')

    if target is None:
        # находим файл target.json
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   request.config.getoption('--target'))
        with open(config_file) as conf:
            target = json.load(conf)

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
# в данном случае ввод значения из консоли и из JSON
def pytest_addoption(parser):
    """функция добавления опции командной строки"""
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')


# получить всю информайцию
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x)
                                                         for x in testdata])


def load_from_module(module):
    return importlib.import_module(f'data.{module}').testdata
