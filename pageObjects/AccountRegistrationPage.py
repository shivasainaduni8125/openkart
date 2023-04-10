from selenium.webdriver.common.by import By
import time

class AccountRegistrationPages():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    chk_news_name = "Sign Up for Newsletter"
    txt_email_id = "email"
    txt_password_name = "password"
    txt_confpassword_id = "password-confirmation"
    btn_create_linktxt="Create an Account"
    # text_msg_conf_class="message-success success message"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self,fname):
      self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setNewsLetter(self):
        self.driver.find_element(By.NAME, self.chk_news_name).click()

    time.sleep(5)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_id).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def setConfirmPassword(self,cnfpwd):
        self.driver.find_element(By.ID,self.txt_confpassword_id).send_keys(cnfpwd)

    def clickCreateAcc(self):
        self.driver.find_element(By.LINK_TEXT,self.btn_create_linktxt).click()


    # def getconfirmationmsg(self):
    #     # try:
    #     return  self.driver.find_element(By.CLASS_NAME,self.text_msg_conf_class).text
    #     # except:




    # def setTelephone(self,tel):
    #    self.driver.find_element(By.NAME,self.txt_telphone_name).send_keys(tel)

    # def setPrivacyPolicy(self):
    #     self.driver.find_element(By.NAME,self.chk_policy_name).click()