from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestOrange:
    def test_logo(self):
        serv_obj = Service("C:/Users/Dell/Documents/Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://opensource-demo.orangehrmlive.com")
        company_logo = driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
        if company_logo == True:
            assert True
        else:
            assert False

    def test_listemployees(self):

    def test_login(self):