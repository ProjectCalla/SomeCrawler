__author__ = 'j'
from somecrawler.config import OsirisConfig, Config, XpathConfig as xpathConf
from lxml import etree
from somecrawler.controller import SeleniumController as sel, RegexController as regex
from somecrawler.crawler.crawl import Base

class OsirisResultsProducer(Base.BaseProducer):
    #TODO clean up and use some hierarchy
    name = OsirisConfig.CONSUMER_NAME
    user = None

    def __init__(self, user):
        Base.BaseProducer.__init__(self)
        self.user = user

    def start(self):
        print "Starting Osiris Results producer"
        return self.getResults(self.setup())

    def setup(self):
        browser = sel.createBrowser()
        browser = sel.login(browser, self.user.username, self.user.password)
        return browser

    def getResults(self, browser):
        browser.get(Config.OSIRIS_RESULTS)
        return browser.page_source



class OsirisResultsConsumer(Base.BaseConsumer):
    name = OsirisConfig.PRODUCER_NAME
    source = None
    user = None
    def __init__(self, user, source):
        Base.BaseConsumer.__init__(self)
        self.sources = source
        self.user = user

    def start(self):
        #TODO fix this
        pass

    def parse(self, source):
        items = {}
        for i in range(2, 17):
            item = {}
            item['test_date'] = source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 1))[0]
            item['course_code'] = source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 2))[0]
            item['course'] = source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 3))[0]
            item['exam_type'] = source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 4))[0]
            item['professor'] = source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 5))[0]
            item['weging'] = source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 6))[0]
            item['result'] = source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 8))[0]
            item['mutation_date'] = source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 10))[0]
            items[str(i)] = item
        return items
