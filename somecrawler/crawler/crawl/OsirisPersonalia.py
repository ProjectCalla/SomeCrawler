__author__ = 'j'
from lxml import etree

from somecrawler.config import OsirisConfig, LinkConfig, XpathConfig as xpath_conf
from somecrawler.crawler.crawl import Base


class OsirisPersonaliaProducer(Base.BaseProducer):
    #TODO clean up and use some hierarchy
    name = OsirisConfig.PRODUCER_NAME
    user = None
    browser = None

    def __init__(self, user, selenium_things):
        Base.BaseProducer.__init__(self)
        self.user = user
        self.browser = selenium_things.browser

    def start(self):
        print "Starting Osiris Personalia producer"
        OsirisPersonaliaConsumer(self.user, self.getPersonalia(self.browser)).start()

    def getPersonalia(self, browser):
        browser.get(LinkConfig.OSIRIS_PERSONALIA)
        return browser.page_source


class OsirisPersonaliaConsumer(Base.BaseConsumer):
    name = OsirisConfig.CONSUMER_NAME
    check = 0

    def start(self):
        self.source = etree.HTML(self.source)
        print self.parse()
        print "start"

    def parse(self):
        personalia = self.parse_default(range(10, 55), self.parse_default(range(1, 9), {}))
        personalia['group'] = self.parseGroup()
        return personalia

    def parseGroup(self):
        group_arr = []
        for i in range(1, 99):
            g = self.source.xpath(xpath_conf.OSIRIS_PERSONALIA_GROUP.format(i))
            if len(g) > 0:
                group_arr.append(g[0])
            else:
                break
        return group_arr

    def parse_default(self, rang, personalia):
        for i in rang:
            g1 = self.source.xpath(xpath_conf.OSIRIS_PERSONALIA_MAIN.format(i, 1))
            g2 = self.source.xpath(xpath_conf.OSIRIS_PERSONALIA_MAIN.format(i, 2))
            if len(g1) == 0 or len(g2) == 0:
                self.some_check()
                continue
            personalia[g1[0]] = g2[0]
        return personalia

    def some_check(self):
        if self.check >= 5:
            return "break"
        self.check += 1



