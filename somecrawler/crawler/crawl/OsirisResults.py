__author__ = 'j'
from somecrawler.config import OsirisConfig, LinkConfig, XpathConfig as xpathConf
from lxml import etree
from somecrawler.controller import SeleniumController as sel, RegexController as regex
from somecrawler.crawler.crawl import Base

class OsirisResultsProducer(Base.BaseProducer):
    #TODO clean up and use some hierarchy
    name = OsirisConfig.CONSUMER_NAME
    user = None
    browser = None

    def __init__(self, user, browser):
        Base.BaseProducer.__init__(self)
        self.user = user
        self.browser = browser

    def start(self):
        print "Starting Osiris Results producer"
        return self.getResults(self.browser)

    def setup(self):
        browser = sel.createBrowser()
        browser = sel.login(browser, self.user.username, self.user.password)
        return browser

    def getResults(self, browser):
        browser.get(LinkConfig.OSIRIS_RESULTS)
        source = browser.page_source
        browser.close()
        return source


class OsirisResultsConsumer(Base.BaseConsumer):
    name = OsirisConfig.PRODUCER_NAME
    source = None
    user = None
    def __init__(self, user, source):
        Base.BaseConsumer.__init__(self)
        self.sources = source
        self.user = user

    def start(self):
        result = self.parse()
        pass

    def parse(self):
        items = {}
        for i in range(2, 17):
            item = {}
            item['test_date'] = self.source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 1))[0]
            item['course_code'] = self.source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 2))[0]
            item['course'] = self.source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 3))[0]
            item['exam_type'] = self.source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 4))[0]
            item['professor'] = self.source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 5))[0]
            item['weging'] = self.source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 6))[0]
            item['result'] = self.source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 8))[0]
            item['mutation_date'] = self.source.xpath(xpathConf.OSIRIS_RESULTS_MAIN.format(i, 10))[0]
            items[str(i)] = item
        return items
