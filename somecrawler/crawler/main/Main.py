from somecrawler.crawler.login import Login

__author__ = 'j'
from somecrawler.crawler.crawl import Osiris
from somecrawler.crawler.config import Config


class Main:
    login = Login.Login()
    osiris = Osiris.OsirisProducer()
    username = Config.USERNAME
    password = Config.PASSWORD
    def __init__(self):
        #Set firefox ~/.mozilla/ prefs.js
        pass
    def fullCrawl(self):

        self.osiris.start()

        #crawls webmail
        #w = Webmail.Webmail()
        #w.start(Config.WEBMAIL_HOME, {})

Main().fullCrawl()