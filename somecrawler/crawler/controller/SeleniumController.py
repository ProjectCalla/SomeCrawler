__author__ = 'j'

import time

from selenium import webdriver
from pyvirtualdisplay import Display

from somecrawler.crawler.config import Config


def login(browser, username, password):
    browser.get(Config.HINT_HOME)
    userId = "username"
    passId = "password"
    submitForm = "submit"
    body = browser.find_element_by_tag_name("body")
    #fill in form
    browser.find_element_by_id(userId).send_keys(username)
    browser.find_element_by_id(passId).send_keys(password)
    browser.find_element_by_id(submitForm).click()
    time.sleep(2)
    return browser

def createBrowser():
    display = Display(visible=0, size=(1024, 768))
    display.start()
    #Initialize browser
    browser = webdriver.Firefox()
    return browser
def closeBrowserFirefox(browser):
    browser.close()
    #pkill firefox
