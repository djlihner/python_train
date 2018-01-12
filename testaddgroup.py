from group import Group
from application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destruct)
    return fixture


def test_add_group(app):
    app.login(user="admin", password="secret")
    app.create_group(Group(name="test1", header="test header", footer="test footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(user="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

