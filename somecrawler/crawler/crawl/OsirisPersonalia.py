__author__ = 'j'
from somecrawler.config import OsirisConfig, LinkConfig, XpathConfig as xpathConf
from lxml import etree
from somecrawler.controller import SeleniumController as sel, RegexController as regex
from somecrawler.crawler.crawl import Base

class OsirisPersonaliaProducer(Base.BaseConsumer):
    #TODO clean up and use some hierarchy
    name = OsirisConfig.CONSUMER_NAME
    user = None

    def __init__(self, user):
        Base.BaseConsumer.__init__(self)
        self.user = user

    def start(self):
        print "Starting Osiris Personalia producer"
        return self.getPersonalia(self.setup())

    def setup(self):
        browser = sel.createBrowser()
        browser = sel.login(browser, self.user.username, self.user.password)
        return browser

    def getPersonalia(self, browser):
        browser.get(LinkConfig.OSIRIS_HOME)
        return browser.page_source

class OsirisPersonaliaConsumer(Base.BaseProducer):
    name = OsirisConfig.PRODUCER_NAME
    source = None
    user = None

    def __init__(self, user, source):
        Base.BaseProducer.__init__(self)
        self.sources = source
        self.user = user

    def start(self):
        print "start"

    def parse(self, source):
        personalia = {}
        group_arr = []
        temp = None
        for i in range(1, 23):
            for x in range(1,3):
                if i == 9 and x == 2:
                    for z in range(1, 10):
                        g = source.xpath(xpathConf.OSIRIS_PERSONALIA_GROUP.format(z))
                        if len(g) > 0:
                            group_arr.append(g[0])
                else:
                    g = source.xpath(xpathConf.OSIRIS_PERSONALIA_MAIN.format(i, x))
                    if len(g) > 0:
                        if x == 1:
                            temp = g[0]
                        else:
                            personalia[temp] = g[0]
        personalia['group'] = group_arr
        personalia.pop('Adres')
        return personalia


