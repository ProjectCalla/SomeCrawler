__author__ = 'j'

import time

from selenium import webdriver
from pyvirtualdisplay import Display

from somecrawler.crawler.config import Config
import logging

def login(browser, username, password):
    logging.info("Logging in ...")
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
    logging.info("Logging in, done.")
    return browser

def createBrowser():
    logging.info("Creating Virtual WebDriver.")
    display = Display(visible=0, size=(1024, 768))
    display.start()
    #Initialize browser
    browser = webdriver.Firefox(setBrowserSettings())
    return browser

def closeBrowserFirefox(browser):
    logging.info("Closing webdriver and killing firefox process.")
    browser.close()
    #pkill firefox

def setBrowserSettings():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    return profile