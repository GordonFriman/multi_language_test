import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or opera")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language, default ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "opera":
        print("\nstart opera browser for test..")
        browser = webdriver.Opera()
    else:
        raise pytest.UsageError("--browser_name should be chrome or opera")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    # link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
    yield language
