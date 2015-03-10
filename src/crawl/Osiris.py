__author__ = 'j'

from src.config import Config
from src.controller import SeleniumController as sel
from lxml import etree
import time
class Osiris:
    def __init__(self):
        pass

    def start(self, session):
        print "start"
        browser = sel.createBrowser()
        browser = sel.login(browser, Config.USERNAME, Config.PASSWORD)
        browser.get(Config.OSIRIS_HOME)
        personalia = self.getPersonalia(browser)
        results = self.getResults(browser)
        self.getStudiepunten(browser)

    def getPersonalia(self, browser):
        #TODO clean up
        personalia = {}
        main = '//*[@id="form0"]/table/tbody/tr/td/table[5]/tbody/tr[2]/td[2]/table[1]/tbody/tr/td[2]/table/tbody/tr[{0}]/td[{1}]/span/text()'
        group = '//*[@id="StudentgroepPerStudent"]/table[2]/tbody/tr[{0}]/td/span/text()'
        source = etree.HTML(browser.page_source)
        group_arr = []
        temp = None
        for i in range(1, 23):
            for x in range(1,3):
                if i == 9 and x == 2:
                    for z in range(1, 10):
                        g = source.xpath(group.format(z))
                        if len(g) > 0:
                            group_arr.append(g[0])
                else:
                    g = source.xpath(main.format(i, x))
                    if len(g) > 0:
                        if x == 1:
                            temp = g[0]
                        else:
                            personalia[temp] = g[0]
        personalia['group'] = group_arr
        personalia.pop('Adres')
        return personalia

    def getResults(self, browser):
        browser.get(Config.OSIRIS_RESULTS)
        source = etree.HTML(browser.page_source)
        date = '//*[@id="ResultatenPerStudent"]/table/tbody/tr/td/table/tbody/tr[{0}]/td[{1}]/span/text()'
        b = {}

        for i in range(2, 17):
            item = {}
            item['test_date'] = source.xpath(date.format(i, 1))[0]
            item['code'] = source.xpath(date.format(i, 2))[0]
            item['course'] = source.xpath(date.format(i, 3))[0]
            item['exam'] = source.xpath(date.format(i, 4))[0]
            item['professor'] = source.xpath(date.format(i, 5))[0]
            item['wage'] = source.xpath(date.format(i, 6))[0]
            item['result'] = source.xpath(date.format(i, 8))[0]
            item['mutation_date'] = source.xpath(date.format(i, 10))[0]
            b[str(i)] = item
        return b

    def getStudiepunten(self, browser):
        total_points = ''
        points = '//*[@id="OpleidingExamenfaseSpecialisatieStudent"]/table/tbody/tr/td/table/tbody/tr[1]/td[7]/a[1]'
        get_js = '//*[@id="OpleidingExamenfaseSpecialisatieStudent"]/table/tbody/tr/td/table/tbody/tr[1]/td[7]/a[1]/@onclick'

        browser.get(Config.OSIRIS_VOORTGANG)

        a = browser.find_element_by_xpath(points).click()
        print "entering sleep"
        time.sleep(10)
        print "stop sleep"

        print browser.page_source

        print etree.HTML(browser.page_source)


