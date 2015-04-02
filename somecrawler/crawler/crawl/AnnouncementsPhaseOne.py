from somecrawler.utils import RegexController as regex

__author__ = 'j'

import time
from lxml import etree

from somecrawler.config import LinkConfig, XpathConfig
from somecrawler.crawler.crawl import Base


class AnnouncementsPhaseOneProducer(Base.BaseProducer):
    #First phase crawler
    user = None
    browser = None

    def __init__(self, user, selenium_things):
        Base.BaseProducer.__init__(self)
        self.user = user
        self.browser = selenium_things.browser

    def start(self):
        self.browser.get(LinkConfig.HINT_HOME)
        time.sleep(15)   #Sleep to wait till the Mededelingen loads
        #TODO check if loading exists
        return etree.HTML(self.browser.page_source)

class AnnouncementsPhaseOneConsumer(Base.BaseConsumer):
    med_code = LinkConfig.MEDEDELINGEN_PHASE_ONE_CODES

    def start(self):
        print "starting consumer Phase One"
        announcements = {}
        for k, v in self.med_code.items():
            announcements[str(k)] = self.parse(str(v)) #ISO has problems
        print announcements
        return announcements

    def parse(self, wid_id):
        med = {}
        med['title'] = regex.mededelingenTitle(str(self.source.xpath(XpathConfig.MEDEDELINGEN_PHASE_ONE_HEADER.format(wid_id))))
        i = 1
        while 1:
            text = self.source.xpath(XpathConfig.MEDEDELINGEN_PHASE_ONE_TEXT.format(wid_id, i))
            title = self.source.xpath(XpathConfig.MEDEDELINGEN_PHASE_ONE_TITLE.format(wid_id, i))
            if len(text) == 0:
                break
            med[regex.filterListUnicode(str(title))] = regex.getNodeNumbers(str(text))
            i += 1
        return med
