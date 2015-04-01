__author__ = 'j'
from somecrawler.config import LinkConfig
from selenium import webdriver
from pyvirtualdisplay import Display
from sys import platform as _platform
import logging, os, time
from lxml import etree
from somecrawler.exception import Exception
import SeleniumThings

def login(selenium_things, username, password):
    print "[SELENIUM_CONTROLLER] Logging in..."
    logging.info("[SELENIUM_CONTROLLER] Logging in ...")
    selenium_things.browser.get(LinkConfig.HINT_HOME)
    #fill in form
    selenium_things.browser.find_element_by_id("username").send_keys(username)
    selenium_things.browser.find_element_by_id("password").send_keys(password)
    selenium_things.browser.find_element_by_id("submit").click()

    if len(str(etree.HTML(selenium_things.browser.page_source).xpath('//*[@id="content"]/div[1]/h5/text()')).replace("[", "").replace("]", "")) > 3:
        raise Exception.LoginException()
    time.sleep(1)
    logging.info("[SELENIUM_CONTROLLER] Logging in, done.")
    return selenium_things

def create_browser():
    print "[SELENIUM_CONTROLLER] Creating browser...."
    logging.info("Creating Virtual WebDriver.")
    display = Display(visible=0, size=(1024, 768))
    display.start()
    return SeleniumThings.JustSeleniumThings(display, webdriver.Firefox(browser_settings()))

def close_browser_firefox1(browser):
    logging.info("[SELENIUM_CONTROLLER] Closing webdriver and killing firefox process.")
    browser.close()

    #This will fuck your browser up if you use firefox for browsing. Disable this
    if _platform == "linux" or _platform == "linux2":
        os.system("pkill firefox")


def browser_settings():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    return profile

