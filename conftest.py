from fixture.application import Application
import pytest

fixture = None


@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(user="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(user="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.__del__()
    request.addfinalizer(fin)
    return fixture
