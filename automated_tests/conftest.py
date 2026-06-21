import pytest
from selenium import webdriver

from .core.api import API
from .core.ui import UI

api_fixture = None
ui_fixture = None
BASE_URL = "https://qae-assignment-tau.vercel.app/"
USER = "candidate-3CybiJF8xy"


@pytest.fixture()
def ui():
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    ui = UI(wd=wd, base_url=BASE_URL, user=USER)
    yield ui

    ui.close()


@pytest.fixture(scope="session")
def api():
    return API(base_url=BASE_URL, user=USER)


@pytest.fixture(autouse=True)
def prepare_balance_for_test(api):
    api.reset_balance()
