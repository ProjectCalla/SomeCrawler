__author__ = 'j'
from somecrawler.config import Config, XpathConfig as xpathConf
from somecrawler.controller import SeleniumController as sel, RegexController as regex
import time
import logging

class WebmailProducer:
    def __init__(self):
        pass

    def start(self, cookies={}):
        if not cookies: cookies = {}
        mailSource = self.getEmails(self.setup(cookies))

    def setup(self, cookies={}):
        browser = sel.createBrowser()
        for c  in cookies:
            cookie_dict = {}
            cookie_dict[c.name] = c.value
            browser.add_cookie(cookie_dict)
        return sel.login(browser, Config.USERNAME, Config.PASSWORD)

    def getEmails(self, browser):
        browser.get(self.correct_url(Config.WEBMAIL_HOME))
        logging.info("Trying to get emails")
        logging.info("Sleeping 15 seconds ...")
        #sleep for
        time.sleep(15)
        logging.info("Done sleeping 15 seconds.")
        browser.maximize_window()
        browser.switch_to.frame(browser.find_element_by_xpath(xpathConf.WEBMAIL_FRAME))
        #not sure what `a = bla bla` does
        a = browser.find_element_by_id("msglist").text
        return browser.page_source

    def correct_url(self, url):
     if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
     return url


class WebmailConsumer:
    webmail_source = None

    def __init__(self, webmail_source):
        self.webmail_source = webmail_source

    def start(self):
        emails = self.parseEmails()

    def parseEmails(self, amount=10):
        emails = {}
        for i in range(1, amount+1):
            item = {}
            for y in range(3, 7):
                item[str(y)] = regex.filterListUnicode(str(self.webmail_source.xpath(xpathConf.WEBMAIL_EMAIL_INFO.format(i,y))))
            emails[str(i)] = item
        return emails
