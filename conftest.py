import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from api import reset_balance
from fixtures.api import API
from fixtures.ui import UI

api_fixture = None
ui_fixture = None
base_url = "https://qae-assignment-tau.vercel.app/"
user = "candidate-3CybiJF8xy"

@pytest.fixture()
def ui(request):
    global ui_fixture
    global user
    global base_url
    if ui_fixture is None:
        wd = webdriver.Chrome()
        wd.implicitly_wait(10)
        ui_fixture = UI(wd=wd, base_url=base_url, user=user)
    return ui_fixture


@pytest.fixture()
def api(request):
    global api_fixture
    global base_url
    global user
    if api_fixture is None:
        api_fixture = API(base_url=base_url, user=user)
    return api_fixture

@pytest.fixture(autouse=True)
def prepare_ui_for_test(api):
    api.reset_balance()

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        if ui_fixture is not None:
            ui_fixture.close()

    request.addfinalizer(fin)
    return ui_fixture