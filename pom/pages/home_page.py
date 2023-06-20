

import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.pages.base_page import BasePages

from typing import List, Tuple, Any
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePages):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver
        self.locator_name_locator: str = '#form-field-name'
        self.locator_email_locator: str = '//input[@id="form-field-myEmail"]'
        self.locator_tel_locator: str = '//input[@id="form-field-number"]'
        self.locator_login_locator: str = '//body/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/div[1]/div[5]/button[1]'


    def load_page(self):
        self.driver.get('https://rt-ed.tech/%D7%A7%D7%95%D7%A8%D7%A1-%D7%91%D7%93%D7%99%D7%A7%D7%95%D7%AA-%D7%AA%D7%95%D7%9B%D7%A0%D7%94-qa_lp/')

    def get_web_element(self,switch:int):

        match switch:
            case 0:
                return self.if_presence(By.CSS_SELECTOR, self.locator_name_locator )

            case 1:
                return self.if_presence(By.XPATH,self.locator_email_locator)

            case 2:
                return self.if_presence(By.XPATH,self.locator_tel_locator)

            case 3:
                return self.if_presence(By.XPATH,self.locator_login_locator)




    #

