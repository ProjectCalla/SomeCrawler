__author__ = 'j'
import requests
from lxml import etree
from ghost import Ghost
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
class Webmail:
    session = None
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    payload = {}
    def __init__(self, session):
        self.session = session
    def crawlWebmail(self):
        pass

    def oldCrawl(self):
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        r = self.session.get("https://webmail.hro.nl")



        print str(etree.HTML(r.text).xpath('/html/body/form/input[1]/@name')).replace("[\'", "").replace("\']", "")
        print str(etree.HTML(r.text).xpath('/html/body/form/input[1]/@value')).replace("[\'", "").replace("\']", "")

        print str(etree.HTML(r.text).xpath('/html/body/form/input[2]/@name')).replace("[\'", "").replace("\']", "")
        print str(etree.HTML(r.text).xpath('/html/body/form/input[2]/@value')).replace("[\'", "").replace("\']", "")

        print str(etree.HTML(r.text).xpath('/html/body/form/input[3]/@name')).replace("[\'", "").replace("\']", "")
        print str(etree.HTML(r.text).xpath('/html/body/form/input[3]/@value')).replace("[\'", "").replace("\']", "")

        print str(etree.HTML(r.text).xpath('/html/body/form/input[4]/@name')).replace("[\'", "").replace("\']", "")
        print str(etree.HTML(r.text).xpath('/html/body/form/input[4]/@value')).replace("[\'", "").replace("\']", "")

        print str(etree.HTML(r.text).xpath('/html/body/form/input[5]/@name')).replace("[\'", "").replace("\']", "")
        print str(etree.HTML(r.text).xpath('/html/body/form/input[5]/@value')).replace("[\'", "").replace("\']", "")

        print str(etree.HTML(r.text).xpath('/html/body/form/input[6]/@name')).replace("[\'", "").replace("\']", "")
        print str(etree.HTML(r.text).xpath('/html/body/form/input[6]/@value')).replace("[\'", "").replace("\']", "")

        print str(etree.HTML(r.text).xpath('/html/body/form/input[7]/@name')).replace("[\'", "").replace("\']", "")
        print str(etree.HTML(r.text).xpath('/html/body/form/input[7]/@value')).replace("[\'", "").replace("\']", "")
        ghost = Ghost()
        page, resources = ghost.open("https://webmail.hro.nl/gw/webacc")
        print 1
        page, resources = ghost.evaluate("gwwa.mlogin.goToBasicInterface()")
        print ghost.content



        r = self.session.post("https://webmail.hro.nl/gw/webacc", data=self.payload)
        print "----------------"
        #print r.text


