__author__ = 'j'
import time
from lxml import etree
from selenium.webdriver.common.keys import Keys
from somecrawler.crawler.config import Config
from somecrawler.crawler.controller import RegexController as regex, SeleniumController as sel
import logging
from somecrawler.crawler.config import XpathConfig as xpathConf

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
        for c  in cookies:
            cookie_dict = {}
            cookie_dict[c.name] = c.value
            browser.add_cookie(cookie_dict)

        #Start crawl
        browser = sel.login(browser, Config.USERNAME, Config.PASSWORD)
        self.getEmails(browser)

        #Browser scroll down -> usage: get all mails, dont forget the wait for the javascript execution
        browser = self.scrollDown(browser, 10)
        browser.quit()


    def getEmails(self, browser):
        browser.get(self.correct_url(self.url))
        logging.info("Trying to get emails")
        logging.info("Sleeping 15 seconds ...")
        #sleep for
        time.sleep(15)
        logging.info("Done sleeping 15 seconds.")
        browser.maximize_window()
        frame = browser.find_element_by_xpath(xpathConf.WEBMAIL_FRAME)

        browser.switch_to.frame(frame)
        a = browser.find_element_by_id("msglist").text
        logging.info("Found source, parsing.")
        emails = self.parseSourceTenEmails(browser)
        logging.info("Done parsing.")
        #write to db etc etc

    def parseSourceTenEmails(self, browser):
        source = etree.HTML(browser.page_source)
        emails = {}
        for i in range(1, 11):
            item = {}
            for y in range(3, 7):
                item[str(y)] = regex.filterListUnicode(str(source.xpath(xpathConf.WEBMAIL_EMAIL_INFO.format(i,y))))
            emails[str(i)] = item
        return emails
