__author__ = 'j'

from lxml import etree
import time
import logging

from selenium.webdriver.common.alert import Alert

from somecrawler.config import LinkConfig, XpathConfig as xpathConf
from somecrawler.controller import RegexController as regex
from somecrawler.crawler.crawl import Base


class WebmailProducer(Base.BaseProducer):
    user = None
    browser = None
    def __init__(self, user, browser):
        Base.BaseProducer.__init__(self)
        self.user = user
        self.browser = browser.browser

    def start(self):
        return self.getEmails()

    def getEmails(self):
        self.browser.get(self.correct_url(LinkConfig.WEBMAIL_HOME))
        logging.info("Trying to get emails")
        logging.info("Sleeping 15 seconds ...")
        time.sleep(2)
        #Alerts
        try:
            Alert(self.browser).accept()
            Alert(self.browser).dismiss()
            logging.info("Alert found on page.. Trying to accept alert.")
        except:
            pass
        logging.info("Done sleeping 15 seconds.")
        self.browser.maximize_window()
        self.browser.switch_to.frame(self.browser.find_element_by_xpath(xpathConf.WEBMAIL_FRAME))

        #browser.find_element_by_id("msglist").text     #old
        return self.browser.page_source

    def correct_url(self, url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        return url


class WebmailConsumer(Base.BaseConsumer):

    def start(self):
        self.source = etree.HTML(self.source)
        emails = self.parse()
        print emails

    def parse(self, amount=10):
        emails = {}
        for i in range(1, amount+1):
            item = {}
            for y in range(3, 7):
                item[str(y)] = regex.filterListUnicode(str(
                    self.source.xpath(xpathConf.WEBMAIL_EMAIL_INFO.format(i, y))))
            emails[str(i)] = item
        return emails
