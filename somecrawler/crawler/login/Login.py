__author__ = 'j'

import requests
from lxml import etree

from somecrawler.crawler.controller import RegexController as regex
from somecrawler.crawler.config import Config


class Login:

    def __init__(self):
        pass

    def login(self, username, password):
        print "trying to log in"
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        payload = {"username" : username, "password" : password}

        #First get login info
        req = session.get(Config.HINT_HOME)
        source = etree.HTML(req.text)
        #adds the payload that is generated to log in

        payload[regex.filterListUnicode(str(source.xpath('//*[@id="formwrap"]/form/div/input[1]/@name')))] = regex.filterListUnicode(str(source.xpath('//*[@id="formwrap"]/form/div/input[1]/@value')))
        payload[regex.filterListUnicode(str(source.xpath('//*[@id="formwrap"]/form/div/input[2]/@name')))] = regex.filterListUnicode(str(source.xpath('//*[@id="formwrap"]/form/div/input[2]/@value')))
        payload[regex.filterListUnicode(str(source.xpath('//*[@id="formwrap"]/form/div/input[3]/@value')))] = regex.filterListUnicode(str(source.xpath('//*[@id="formwrap"]/form/div/input[3]/@value')))

        #login
        session.post(Config.HINT_LOGIN, data=payload)
        return session