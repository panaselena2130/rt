
from selenium.webdriver.common.by import  By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing import List
import time

class BasePages:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def webelement_by(self, find_by: str) -> dict:
        find_by = find_by.lower()

        locating = {'xpath': By.XPATH,
                    'css': By.CSS_SELECTOR,
                    'class':By.CLASS_NAME}

        return locating[find_by]




    def if_presence(self, key: object, locator: object)-> WebElement:
        return self.wait.until(EC.presence_of_element_located((key,locator)))



    def click_element(self,button)->WebElement:
      return self.wait.until(EC.element_to_be_clickable((button))).click()


    def screen_shot(self,name):
        timestr = time.strftime('%Y-%m-%d-%H.%M.%S')

        time.sleep(2)
        self.driver.save_screenshot(f".{name, timestr}.png")
