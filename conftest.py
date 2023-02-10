# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseUrl')
    username = request.config.getoption('--username')
    password = request.config.getoption('--password')
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)

    fixture.session.ensure_login(username=username, password=password)
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
    parser.addoption("--baseUrl", action="store",
                     default='http://localhost/addressbook/')
    parser.addoption("--username", action="store", default='admin')
    parser.addoption("--password", action="store", default='secret')
