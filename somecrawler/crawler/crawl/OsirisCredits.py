__author__ = 'j'
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