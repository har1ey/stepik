import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
    Встроенная фикстура request может получать данные о текущем запущенном тесте, что позволяет,
    например, сохранять дополнительные данные в отчёт, и др..
    https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption
"""


def pytest_addoption(parser):
    """
    запуск :
        pytest -v --tb=line --browser_name=chrome --language=en -m need_review
    по умолчанию браузер 'chrome' и язык 'en'
        pytest -v --tb=line -m need_review
    """
    parser.addoption('--language', action='store', default='en',
                     help="Please set language, example 'es'")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
