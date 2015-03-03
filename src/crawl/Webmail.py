__author__ = 'j'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from src.config import Config
import time
import requests

class Webmail:
    url = None
    def __init__(self):
        pass

    def correct_url(self, url):
     if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
     return url

    def scrollDown(self, browser, numberOfScrollDowns):
        body = browser.find_element_by_tag_name("body")
        while numberOfScrollDowns >=0:
            body.send_keys(Keys.PAGE_DOWN)
            numberOfScrollDowns -= 1
        return browser

    def crawl_url(self, url, cookies, run_headless=True):
        self.url = url
        if run_headless:
            display = Display(visible=0, size=(1024, 768))
            display.start()

        #Initialize browser

        browser = webdriver.Firefox()
        browser.get(self.correct_url(self.url))

        #Adding cookie
        cookieDict = {}
        for c  in cookies:
            cookieDict.clear()
            cookieDict[c.name] = c.value
            browser.add_cookie(cookieDict)

        #Start crawl
        browser = self.login(browser)
        self.getEmails(browser)

        #Browser scroll down -> usage: get all mails, dont forget the wait for the javascript execution
        browser = self.scrollDown(browser, 10)
        browser.quit()

    def login(self, browser):
        userId = "username"
        passId = "password"
        submitForm = "submit"
        body = browser.find_element_by_tag_name("body")
        #fill in form
        browser.find_element_by_id(userId).send_keys(Config.USERNAME)
        browser.find_element_by_id(passId).send_keys(Config.PASSWORD)
        browser.find_element_by_id(submitForm).click()
        return browser


    def getEmails(self, browser):
        browser.get(self.correct_url(self.url))
        print self.url
        #sleep for
        time.sleep(15)

        browser.maximize_window()
        frame = browser.find_element_by_xpath('//*[@id="idWebAccFrameset"]/frame[2]')
        print frame.text
        browser.switch_to.frame(frame)

        print browser.find_element_by_id("msglist").text
        #return browser on login

