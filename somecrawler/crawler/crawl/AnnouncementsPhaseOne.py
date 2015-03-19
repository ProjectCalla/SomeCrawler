__author__ = 'j'
from somecrawler.config import Config, XpathConfig
import time
from lxml import etree
from somecrawler.controller import SeleniumController as sel, RegexController as regex
from somecrawler.crawler.crawl import Base
class AnnouncementsPhaseOneProducer(Base.BaseProducer):
    #First phase crawler
    def __init__(self):
        Base.BaseProducer.__init__(self)

    def start(self):
        browser = self.setup()
        browser.get(Config.HINT_HOME)
        time.sleep(15)   #Sleep to wait till the Mededelingen loads
        #TODO check if loading exists
        return browser.page_source

    def setup(self):
        browser = sel.createBrowser()
        return sel.login(browser, Config.USERNAME, Config.PASSWORD)


class AnnouncementsPhaseOneConsumer(Base.BaseConsumer):
    source = None
    med_code = Config.MEDEDELINGEN_PHASE_ONE_CODES
    def __init__(self, source):
        Base.BaseConsumer.__init__(self)
        self.source = source

    def start(self):
        announcements = {}
        for k,v in self.med_code.items():
            announcements[str(k)] = self.parse(self.source, str(v)) #ISO has problems
        print announcements

    def parse(self, html, wid_id):
        med = {}
        source = etree.HTML(html)
        med['title'] = regex.mededelingenTitle(str(source.xpath(XpathConfig.MEDEDELINGEN_PHASE_ONE_HEADER.format(wid_id))))

        i = 1
        while 1:
            text = source.xpath(XpathConfig.MEDEDELINGEN_PHASE_ONE_TEXT.format(wid_id, i))
            title = source.xpath(XpathConfig.MEDEDELINGEN_PHASE_ONE_TITLE.format(wid_id, i))
            if len(text) == 0:
                break
            med[regex.filterListUnicode(str(title))] = regex.getNodeNumbers(str(text))
            i += 1
        return med

