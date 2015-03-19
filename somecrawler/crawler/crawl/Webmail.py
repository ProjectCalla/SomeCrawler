__author__ = 'j'
from somecrawler.config import Config, XpathConfig as xpathConf
from somecrawler.controller import SeleniumController as sel, RegexController as regex
import time
import logging
from somecrawler.crawler.crawl import Base
from selenium.webdriver.common.alert import Alert

class WebmailProducer(Base.BaseProducer):
    user = None
    def __init__(self, user):
        Base.BaseProducer.__init__(self)
        self.user = user

    def start(self, cookies={}):
        if not cookies: cookies = {}
        return self.getEmails(self.setup(cookies))

    def setup(self, cookies={}):
        browser = sel.createBrowser()
        for c  in cookies:
            cookie_dict = {}
            cookie_dict[c.name] = c.value
            browser.add_cookie(cookie_dict)
        return sel.login(browser, self.user.username, self.user.password)

    def getEmails(self, browser):
        browser.get(self.correct_url(Config.WEBMAIL_HOME))
        logging.info("Trying to get emails")
        logging.info("Sleeping 15 seconds ...")
        #sleep for
        time.sleep(15)

        #Alerts
        try:
            Alert(browser).accept()
            logging.info("Alert found on page.. Trying to accept alert.")
        except:
            pass
        logging.info("Done sleeping 15 seconds.")
        browser.maximize_window()
        browser.switch_to.frame(browser.find_element_by_xpath(xpathConf.WEBMAIL_FRAME))
        #not sure what `a = bla bla` does
        #browser.find_element_by_id("msglist").text     #old

        return browser.page_source

    def correct_url(self, url):
     if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
     return url


class WebmailConsumer(Base.BaseConsumer):
    webmail_source = None

    def __init__(self, webmail_source):
        Base.BaseConsumer.__init__(self)
        self.webmail_source = webmail_source

    def start(self):
        emails = self.parse()

    def parse(self, amount=10):
        emails = {}
        for i in range(1, amount+1):
            item = {}
            for y in range(3, 7):
                item[str(y)] = regex.filterListUnicode(str(self.webmail_source.xpath(xpathConf.WEBMAIL_EMAIL_INFO.format(i,y))))
            emails[str(i)] = item
        return emails
