__author__ = 'j'

from src.login import Login
import time
from src.config import Config
from src.controller import SeleniumController as sel
from lxml import etree
from src.controller import RegexController as regex

class Mededelingen:
    #TODO clean up. make configs, do something
    wdk_wid_id = "wid_1376787"
    rmu_wid_id = "wid_1376786"
    rbs_wid_id = "wid_1376785"
    cmi_wid_id = "wid_980848"
    rac_wid_id = "wid_1376784"
    ivl_wid_id = "wid_1376783"
    ifm_wid_id = "wid_1376779"
    com_wid_id = "wid_1376776"
    eas_wid_id = "wid_1376777"
    ibk_wid_id = "wid_1376778"
    ivg_wid_id = "wid_1376782"
    igo_wid_id = "wid_1376780"
    iso_wid_id = "wid_1376781"

    login = Login.Login()

    def __init__(self):
        pass

    def getAllMededelingen(self):
        browser = sel.createBrowser()
        browser = sel.login(browser, Config.USERNAME, Config.PASSWORD)
        browser.get("http://hint.hro.nl")
        time.sleep(15)   #Sleep to wait till the Mededelingen loads
        html = browser.page_source  #TODO check if loading exists

        print self.getMededelingen(html, self.wdk_wid_id)
        print self.getMededelingen(html, self.rmu_wid_id)
        print self.getMededelingen(html, self.rbs_wid_id)
        print self.getMededelingen(html, self.cmi_wid_id)
        print self.getMededelingen(html, self.rac_wid_id)
        print self.getMededelingen(html, self.ivl_wid_id)
        print self.getMededelingen(html, self.ifm_wid_id)
        print self.getMededelingen(html, self.com_wid_id)
        print self.getMededelingen(html, self.eas_wid_id)
        print self.getMededelingen(html, self.ibk_wid_id)
        print self.getMededelingen(html, self.ivg_wid_id)
        print self.getMededelingen(html, self.igo_wid_id)
        print self.getMededelingen(html, self.iso_wid_id)

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