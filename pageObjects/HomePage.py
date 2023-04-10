from selenium.webdriver.common.by import By


class HomePages():
    # lnk_myaccount_intext = "My Account"
    lnk_register_linktext = "Create an Account"
    lnk_login_linktext = "Sign In"


    def __init__(self, driver):
        self.driver = driver

    # def clickMyAccount(self):
    #     self.driver.find_element(By.LINK_TEXT, self.lnk_myaccount_intext).click()

    def clickCreateAcc(self):
        self.driver.find_element
    def clickSignIn(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
