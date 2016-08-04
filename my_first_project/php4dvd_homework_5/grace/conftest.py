import pytest


def pytest_addoption(parser):
    parser.addoption('--browser', default='firefox')
    parser.addoption('--base_url', default='http://localhost/php4dvd/')


@pytest.fixture(scope='module')
def browser_type(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='module')
def base_url(request):
    return request.config.getoption('--base_url')