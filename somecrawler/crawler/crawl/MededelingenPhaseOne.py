__author__ = 'j'
from somecrawler.crawler.controller import RegexController as regex, SeleniumController as sel
from somecrawler.crawler.login import Login
import time
from somecrawler.crawler.config import Config
from lxml import etree


class Mededelingen:
    #First phase crawler
    #TODO clean up. make configs, do something
    med_code = Config.MEDEDELINGEN_PHASE_ONE_LINKS

    login = Login.Login()

    def __init__(self):
        pass

    def getAllMededelingen(self):
        browser = sel.createBrowser()
        browser = sel.login(browser, Config.USERNAME, Config.PASSWORD)
        browser.get("http://hint.hro.nl")
        time.sleep(15)   #Sleep to wait till the Mededelingen loads
        html = browser.page_source  #TODO check if loading exists
        #TODO loop the crap
        print self.getMededelingen(html, self.med_code['wdk_wid_id'])
        print self.getMededelingen(html, self.med_code['rmu_wid_id'])
        print self.getMededelingen(html, self.med_code['rbs_wid_id'])
        print self.getMededelingen(html, self.med_code['cmi_wid_id'])
        print self.getMededelingen(html, self.med_code['rac_wid_id'])
        print self.getMededelingen(html, self.med_code['ivl_wid_id'])
        print self.getMededelingen(html, self.med_code['ifm_wid_id'])
        print self.getMededelingen(html, self.med_code['com_wid_id'])
        print self.getMededelingen(html, self.med_code['eas_wid_id'])
        print self.getMededelingen(html, self.med_code['ibk_wid_id'])
        print self.getMededelingen(html, self.med_code['ivg_wid_id'])
        print self.getMededelingen(html, self.med_code['igo_wid_id'])
        print self.getMededelingen(html, self.med_code['iso_wid_id'])

        browser.close()

    def getMededelingen(self, html, wid_id):
        med = {}
        source = etree.HTML(html)
        text = source.xpath('//*[@id="'+wid_id+'"]/div[1]/h3/span[1]/text()')
        med_title = regex.mededelingenTitle(str(text))
        med['title'] = med_title

        i = 1
        while 1:
            text = source.xpath('//*[@id="'+wid_id+'"]/div[2]/div/div/ul/li[%s]/@class' % i)
            title = source.xpath('//*[@id="'+wid_id+'"]/div[2]/div/div/ul/li[%s]/h4/text()' % i)
            if len(text) == 0:
                break
            med[regex.filterListUnicode(str(title))] = regex.getNodeNumbers(str(text))
            i += 1
        return med

Mededelingen().getAllMededelingen()