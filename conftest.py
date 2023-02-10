# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture

    if fixture is None:
        browser = request.config.getoption("--browser")
        fixture = Application(browser=browser)
    else:
        if not fixture.is_valid():
            fixture = Application()

    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


# autouse=True - автом. использование метода
@pytest.fixture(scope="session", autouse=True)
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
    parser.addoption("--browser", action="store",
                     default="firefox")
