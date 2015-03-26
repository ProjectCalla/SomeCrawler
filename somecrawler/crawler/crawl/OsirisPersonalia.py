__author__ = 'j'
from somecrawler.config import OsirisConfig, LinkConfig, XpathConfig as xpath_conf
from lxml import etree
from somecrawler.controller import SeleniumController as sel, RegexController as regex
from somecrawler.crawler.crawl import Base

class OsirisPersonaliaProducer(Base.BaseProducer):
    #TODO clean up and use some hierarchy
    name = OsirisConfig.PRODUCER_NAME
    user = None
    browser = None

    def __init__(self, user, browser):
        Base.BaseProducer.__init__(self)
        self.user = user
        self.browser = browser

    def start(self):
        print "Starting Osiris Personalia producer"
        return self.getPersonalia(self.browser)

    def getPersonalia(self, browser):
        browser.get(LinkConfig.OSIRIS_HOME)
        source = browser.page_source
        browser.close()
        return source

class OsirisPersonaliaConsumer(Base.BaseProducer):
    name = OsirisConfig.CONSUMER_NAME
    source = None
    user = None

    def __init__(self, user, source):
        Base.BaseProducer.__init__(self)
        self.sources = source
        self.user = user

    def start(self):
        print "start"

    def parse(self):
        personalia = {}
        group_arr = []
        temp = None
        for i in range(1, 23):
            for x in range(1,3):
                if i == 9 and x == 2:
                    for z in range(1, 10):
                        g = self.source.xpath(xpath_conf.OSIRIS_PERSONALIA_GROUP.format(z))
                        if len(g) > 0:
                            group_arr.append(g[0])
                else:
                    g = self.source.xpath(xpath_conf.OSIRIS_PERSONALIA_MAIN.format(i, x))
                    if len(g) > 0:
                        if x == 1:
                            temp = g[0]
                        else:
                            personalia[temp] = g[0]
        personalia['group'] = group_arr
        personalia.pop('Adres')
        return personalia


