__author__ = 'j'

from selenium.webdriver.common.keys import Keys
from src.config import Config
import time

from src.controller import SeleniumController as sel
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

    def start(self, url, cookies):
        self.url = url
        browser = sel.createBrowser()


        #Adding cookie
        cookieDict = {}
        for c  in cookies:
            cookieDict.clear()
            cookieDict[c.name] = c.value
            browser.add_cookie(cookieDict)

        #Start crawl
        browser = sel.login(browser, Config.USERNAME, Config.PASSWORD)
        self.getEmails(browser)

        #Browser scroll down -> usage: get all mails, dont forget the wait for the javascript execution
        browser = self.scrollDown(browser, 10)
        browser.quit()


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
        #write to db etc etc

