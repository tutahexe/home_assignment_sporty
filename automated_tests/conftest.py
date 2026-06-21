import pytest
from selenium import webdriver

from .core.api import API
from .core.ui import UI


@pytest.fixture()
def ui(base_url, user):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    ui = UI(wd=wd, base_url=base_url, user=user)
    yield ui

    ui.close()


@pytest.fixture(scope="session")
def api(base_url, user):
    return API(base_url=base_url, user=user)


@pytest.fixture(autouse=True)
def prepare_balance_for_test(api):
    api.reset_balance()


def pytest_addoption(parser):
    parser.addini("base_url", help="Base URL")
    parser.addini("user", help="Test user")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getini("base_url")


@pytest.fixture(scope="session")
def user(request):
    return request.config.getini("user")
