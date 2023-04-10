import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #ChromeDriverManager is a class had a method called install.
    return driver

