# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application


fixture = None

# @pytest.fixture(scope="session")
@pytest.fixture
def app(request):
    global fixture

    if fixture is None:
        fixture = Application()
    elif not fixture.is_valid():
        fixture = Application()
    fixture.session.ensure_login(username='admin', password='secret')
    return fixture

# autouse=True - автом. использование метода
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logaut()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
