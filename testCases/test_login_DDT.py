import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen
from utilities import XLUtility


class Test_002_DDT_Login:
    base_url = ReadConfig.get_application_url()
    path = "./TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)

        self.row = XLUtility.getRowCount(self.path, "Sheet1")
        list_status = []

        for r in range(2, self.row+1):
            self.user = XLUtility.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtility.readData(self.path, 'Sheet1', r, 2)
            self.exp_value = XLUtility.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLoginButton()
            time.sleep(3)
            # validate welcome page
            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            print(f"actual_title ---> {actual_title}")
            print(f"self.exp_value ---> {self.exp_value}")
            print("Before 40th line")
            if actual_title == exp_title:
                print("Before 41 line")
                if self.exp_value == 'pass':
                    print("Before 43th line")
                    self.lp.clickLogout()
                    list_status.append("pass")
                    print(f"list_status inside if if -->{list_status}")
                elif self.exp_value == 'fail':
                    self.lp.clickLogout()
                    list_status.append("fail")
            elif actual_title != exp_title:
                if self.exp_value == 'pass':
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    list_status.append("fail")
                elif self.exp_value == 'fail':
                    list_status.append("pass")
        if 'fail' not in list_status:
            self.logger.info("Data Driven Test pass")
            print(f"list_status out of for loop ---> {list_status} ")
            self.driver.close()
            assert True
        else:
            self.logger.info("Data Driven Test failed")
            print(f"list_status ---> {list_status} ")
            self.driver.close()
            assert False


            #     self.logger.info("***** Data Driven Test is pass *****")
            #     assert True
            #     self.driver.close()
            # else:
            #     self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            #     self.driver.close()
            #     assert False
