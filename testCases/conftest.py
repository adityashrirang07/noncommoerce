import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def setup(browser):
    if browser == 'firefox':
        serv_object = Service("C:/Users/Dell/Documents/Drivers/geckodriver.exe")
        driver = webdriver.Firefox(service=serv_object)
    else:
        serv_object = Service("C:/Users/Dell/Documents/Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=serv_object)
    return driver
    # else:
    #     serv_object = Service("C:/Users/Dell/Documents/Drivers/chromedriver.exe")
    #     driver = webdriver.Chrome(service=serv_object)
    #return driver

def pytest_addoption(parser):
    parser.addoption("--browser") #it will get value from browser

@pytest.fixture()
def browser(request): #this method will return value to setup method
    return request.config.getoption("--browser")

############### pytest HTML report #############
# it's a hook for adding Environment info to report
# def pytest_configure(config):
#     config._metadata['Project Name'] = "nop commerce"
#     config._metadata['Module Name'] = "Customers"
#     config._metadata['Tester'] = "Savitha"

#It's a hook for delete/modify Environment info in report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

