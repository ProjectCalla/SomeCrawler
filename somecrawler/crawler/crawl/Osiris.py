__author__ = 'j'

from lxml import etree

from somecrawler.crawler.config import Config, XpathConfig as xpathConf, OsirisConfig
from somecrawler.crawler.controller import SeleniumController as sel, RegexController as regex


class OsirisProducer:
    name = OsirisConfig.CONSUMER_NAME
    username = None
    password = None

    def __init__(self):
        pass

    def start(self):
        #add and use password
        print "Starting Osiris Consumer"
        browser = sel.createBrowser()
        browser = sel.login(browser, Config.USERNAME, Config.PASSWORD)
        browser.get(Config.OSIRIS_HOME)

        personalia = self.getPersonalia(browser)
        results = self.getResults(browser)

    def getPersonalia(self, browser):
        source = etree.HTML(browser.page_source)
        return source

    def getResults(self, browser):
        browser.get(Config.OSIRIS_RESULTS)
        source = etree.HTML(browser.page_source)
        return source

"""
#Probably not needed anymore
    def getCredits(self, browser):
        #need more voortgang to match it
        points = '//*[@id="OpleidingExamenfaseSpecialisatieStudent"]/table/tbody/tr/td/table/tbody/tr[2]/td[7]/a[1]'
        credit_elements_inf2 = {'date': 11, 'course':17, 'min_points':53, 'curent_points':54}
        xpath_main = '//*[@id="form0"]/div[{0}]/span/text()'

        browser.get(Config.OSIRIS_VOORTGANG)
        browser.find_element_by_xpath(points).click()
        browser.get(Config.OSIRIS_VOORTGANG_EMBEDDEDREPORT)

        source = etree.HTML(browser.page_source)
        print regex.filterXao(regex.filterOsirisEmbeddedReportUnicode(str(source.xpath(STR))), "")
"""

class OsirisConsumer:
    name = OsirisConfig.PRODUCER_NAME
    sources = {}

    def __init__(self, sources):
        self.sources = sources

    def start(self):

        pass

    def parsePersonlia(self, source):
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
        print personalia
        return personalia
        pass

    def parseResults(self, source):
        date = '//*[@id="ResultatenPerStudent"]/table/tbody/tr/td/table/tbody/tr[{0}]/td[{1}]/span/text()'
        items = {}

        for i in range(2, 17):
            item = {}
            item['test_date'] = source.xpath(date.format(i, 1))[0]
            item['course_code'] = source.xpath(date.format(i, 2))[0]
            item['course'] = source.xpath(date.format(i, 3))[0]
            item['exam_type'] = source.xpath(date.format(i, 4))[0]
            item['professor'] = source.xpath(date.format(i, 5))[0]
            item['weging'] = source.xpath(date.format(i, 6))[0]
            item['result'] = source.xpath(date.format(i, 8))[0]
            item['mutation_date'] = source.xpath(date.format(i, 10))[0]
            items[str(i)] = item
        return items
