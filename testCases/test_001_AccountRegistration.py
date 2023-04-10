from pageObjects.HomePage import HomePages
from pageObjects.AccountRegistrationPage import AccountRegistrationPages
from utilities import randomeString
import os

class Test_001_AccountReg:
    baseURL = "https:demo.opencart.com/"

    def test_account_reg(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        #HomePage
        self.hp=HomePages(self.driver)
        self.hp.clickCreateAcc()


        #AccountRegistrationPage
        self.regpage=AccountRegistrationPages(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email=randomeString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("ontario@2023")
        self.regpage.setConfirmPassword("ontario@2023")
        self.regpage.clickCreateAcc()
        # self.confmsg=self.regpage.getconfirmationmsg()
        self.driver.close()

        # if self.confmsg=="Thank you for registering with Main Website Store.":
        #     assert True
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//"+"test_account_reg")
        #     assert False






