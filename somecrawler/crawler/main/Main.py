from somecrawler.crawler.login import Login

__author__ = 'j'
from somecrawler.crawler.crawl import Osiris
from somecrawler.crawler.config import Config


class Main:
    login = Login.Login()
    osiris = Osiris.Osiris()
    username = Config.USERNAME
    password = Config.PASSWORD
    def __init__(self):
        #Set firefox ~/.mozilla/ prefs.js
        pass
    def fullCrawl(self):
        session = self.login.login(self.username, self.password)
        f = session.get(Config.HINT_HOME)
        self.osiris.start(session)

        #crawls webmail
        #w = Webmail.Webmail()
        #w.start(Config.WEBMAIL_HOME, {})

Main().fullCrawl()