__author__ = 'j'
from somecrawler.config import LinkConfig
import time
from selenium import webdriver
from pyvirtualdisplay import Display
from sys import platform as _platform
import logging, os

def login(browser, username, password):
    print "[SELENIUM_CONTROLLER] Logging in..."
    logging.info("Logging in ...")
    browser.get(LinkConfig.HINT_HOME)
    #fill in form
    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_id("submit").click()
    time.sleep(2)
    logging.info("Logging in, done.")
    return browser

def createBrowser():
    print "[SELENIUM_CONTROLLER] Creating browser...."
    logging.info("Creating Virtual WebDriver.")
    display = Display(visible=0, size=(1024, 768))
    display.start()
    #Initialize browser
    browser = webdriver.Firefox(setBrowserSettings())
    return browser

def closeBrowserFirefox1(browser):
    logging.info("Closing webdriver and killing firefox process.")
    browser.close()

    #This will fuck your browser up if you use firefox for browsing. Disable this
    if _platform == "linux" or _platform == "linux2":
        os.system("pkill firefox")

def setBrowserSettings():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    return profile