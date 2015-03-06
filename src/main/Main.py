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
        f = session.get("https://hint.hro.nl")

        #crawls webmail
        w = Webmail.Webmail()
        w.start("https://webmail.hro.nl", {})



Main().fullCrawl()