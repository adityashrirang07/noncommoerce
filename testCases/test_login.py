import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen


class Test_001_Login:
    base_url = ReadConfig.get_application_url()
    user_name = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    def test_home_page_title(self, setup):
        self.logger.info('Logging....... !!!!!!!!!!!!!!!')
        self.logger.info("*** Login mechanism implemented successfully ***")
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Your store. Login":
            self.logger.info("---Validation success----")
            self.logger.debug("---Validation success----")
            self.logger.critical("---Validation success----")
            self.logger.warning("---Validation success----")

            assert True
        else:
            self.driver.save_screenshot("./Screenshots" + "test_home_page_title.png")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.user_name)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        # validate welcome page
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            assert False
