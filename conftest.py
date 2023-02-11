# -*- coding: utf-8 -*-
import pytest
import json


from fixture.application import Application


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    if target is None:
        with open(request.config.getoption('--target')) as conf:
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
    parser.addoption("--target", action="store", default='target.json')
    parser.addoption("--target", action="store", default='target.json')
