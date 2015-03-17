__author__ = 'j'
from somecrawler.config import OsirisConfig, Config, XpathConfig as xpathConf
from lxml import etree
from somecrawler.controller import SeleniumController as sel, RegexController as regex

class OsirisProducer:
    name = OsirisConfig.CONSUMER_NAME
    username = None
    password = None

    def __init__(self):
        pass

    def startPersonalia(self):
        print "Starting Osiris Personalia producer"
        return self.getPersonalia(self.setup())

    def startResults(self):
        print "Starting Osiris Results producer"
        return self.getResults(self.setup())

    def setup(self):
        browser = sel.createBrowser()
        browser = sel.login(browser, Config.USERNAME, Config.PASSWORD)
        return browser
    def getPersonalia(self, browser):
        browser.get(Config.OSIRIS_HOME)
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
        return personalia

    def parseResults(self, source):
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
