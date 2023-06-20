import time
import datetime

from pom.pages.home_page import HomePage

name = 'test'
email = 'test@rt-ed.co.il'
numb_tel = '0505000000'


def test_login(driver):
    homepage = HomePage(driver)
    homepage.load_page()
    homepage.get_web_element(0).send_keys(name)
    time.sleep(3)
    homepage.get_web_element(1).send_keys(email)
    time.sleep(3)
    homepage.get_web_element(2).send_keys(numb_tel)
    time.sleep(3)
    TalkToMe = homepage.get_web_element(3)
    time.sleep(3)

    homepage.click_element(TalkToMe)


    homepage.screen_shot("Screen")







