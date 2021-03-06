__author__ = 'j'
from somecrawler.config import OsirisConfig, LinkConfig, XpathConfig as xpathConf
from lxml import etree
from somecrawler.crawler.crawl import Base


class OsirisResultsProducer(Base.BaseProducer):
    name = OsirisConfig.PRODUCER_NAME
    user = None
    browser = None

    def __init__(self, user, selenium_things):
        Base.BaseProducer.__init__(self)
        self.user = user
        self.browser = selenium_things.browser

    def start(self):
        print "Starting Osiris Results producer"
        return self.getResults(self.browser)

    def getResults(self, browser):
        browser.get(LinkConfig.OSIRIS_RESULTS)
        return etree.HTML(browser.page_source)


class OsirisResultsConsumer(Base.BaseConsumer):
    name = OsirisConfig.CONSUMER_NAME

    def start(self):
        result = self.parse()

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
        print items
        return items
