__author__ = 'j'
from src.login import Login
from src.crawl import Webmail
from src.config import Config


class Main:
    login = Login.Login()
    username = Config.USERNAME
    password = Config.PASSWORD
    def __init__(self):
        #Set firefox ~/.mozilla/ prefs.js
        pass
    def fullCrawl(self):
        session = self.login.login(self.username, self.password)

        #crawls webmail
        w = Webmail.Webmail()
        w.crawl_url("https://webmail.hro.nl", session.cookies)



Main().fullCrawl()