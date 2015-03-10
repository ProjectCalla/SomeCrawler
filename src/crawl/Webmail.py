__author__ = 'j'

from selenium.webdriver.common.keys import Keys
from src.config import Config
import time
from src.controller import RegexController as regex
from lxml import etree
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
        a = browser.find_element_by_id("msglist").text

        emails = self.parseSourceTenEmails(browser)

        #write to db etc etc

    def parseSourceTenEmails(self, browser):
        source = etree.HTML(browser.page_source)
        mail_table = '//*[@id="msglist"]/div[1]/div/table/tbody/tr[%s]'
        email_info = '//*[@id="msglist"]/div[1]/div/table/tbody/tr[{0}]/td[{1}]/text()'
        emails = {}
        for i in range(1, 11):
            item = {}
            for y in range(3, 7):
                item[str(y)] = regex.filterListUnicode(str(source.xpath(email_info.format(i,y))))
            emails[str(i)] = item
        return emails
