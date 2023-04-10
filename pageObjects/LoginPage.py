from selenium.webdriver.common.by import By
from selenium import webdriver
from pageObjects.AccountRegistrationPage import AccountRegistrationPages
import time

class LoginPages():
    txt_emailInput_name = "email"
    txt_passwordInput_name = "password"
    btn_signIn_name = "send"

    def __init__(self, driver):
        self.driver = driver

    #Action methods
    def emailInput(self,username):
        self.driver.find_element(By.NAME,self.txt_emailInput_name).clear()
        self.driver.find_element(By.NAME,self.txt_emailInput_name).send_keys(username)

    def pwdInput(self,password):
        self.driver.find_element(By.NAME, self.txt_passwordInput_name).clear()
        self.driver.find_element(By.NAME,self.txt_passwordInput_name).send_keys(password)
    def clicksignIn(self):
        self.driver.find_element(By.CLASS_NAME,self.btn_signIn_name)



