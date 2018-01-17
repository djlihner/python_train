from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(user="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.__del__()
    request.addfinalizer(fin)
    return fixture
