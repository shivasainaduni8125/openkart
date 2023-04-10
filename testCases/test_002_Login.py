from pageObjects.HomePage import HomePages
from pageObjects.LoginPage import LoginPages
from utilities.readProperties import ReadConfig
import pytest
from selenium import webdriver

#every test caseID should be unique
class Test_002_Login:


    def test_account_login(self,setup):
        self.driver= setup
        self.driver.maximize_window()

        # HomePage
        self.hp = HomePages(self.driver)
        self.hp.clickSignIn()

        #Login
        #below is object of loginpageclass
        self.logCredentials = ReadConfig()
        self.signIn = LoginPages(self.driver)


        self.logCredentials.LoginID()
        self.logCredentials.LoginPwd()
        self.signIn.clicksignIn()
