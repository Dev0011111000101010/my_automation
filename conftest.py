import selenium, pytest, webdriver_manager, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_is_SELENIUM_installed_and_what_version():
    """
    Function requires "import selenium" + #pip3 install selenium
    Function checks if the project has Selenium installed
    And if yes, what version
    The result is output to the console.
    Example: "
    1. "Selenium" installed successfully;
    2. "Selenium" imported successfully;
    3. "Selenium" version is = 4.8.3 "
    """
    print('\n1. "Selenium" installed successfully; \n'
          '2. "Selenium" imported successfully;  \n'
          '3. "Selenium" version is =', selenium.__version__, '\n')
test_is_SELENIUM_installed_and_what_version()

def test_is_PYTEST_installed_and_what_version():
    """
    Function requires "import pytest" + #pip3 install pytest
    Function checks if the project has Pytest installed
    And if yes, what version
    The result is output to the console.
    Example: "
    1. "Pytest" installed successfully;
    2. "Pytest" imported successfully;
    3. "Pytest" version is = 7.2.2 "
    """
    print('\n1. "Pytest" installed successfully; \n'
          '2. "Pytest" imported successfully;  \n'
          '3. "Pytest" version is =', pytest.__version__, '\n')
test_is_PYTEST_installed_and_what_version()

def test_is_WEBDRIVER_MANAGER_installed_and_what_version():
    """
    Function requires "import webdriver_manager" + #pip3 install webdriver_manager (#pip3 install webdriver-manager)
    Function checks if the project has Webdriver_manager installed
    And if yes, what version
    The result is output to the console.
    Example: "
    1. "Webdriver_manager" installed successfully;
    2. "Webdriver_manager" imported successfully;
    3. "Webdriver_manager" version is = 3.8.5 "
    """
    print('\n1. "Webdriver_manager" installed successfully; \n'
          '2. "Webdriver_manager" imported successfully;  \n'
          '3. "Webdriver_manager" version is =', webdriver_manager.__version__, '\n')
test_is_WEBDRIVER_MANAGER_installed_and_what_version()

# @pytest.fixtura(scope='function')
@pytest.fixture(scope='function')
def driver():
    print('=============================Start Browser=============================locators.py')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    time.sleep(2)
    yield driver
    time.sleep(2)
    driver.quit()
