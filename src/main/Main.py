__author__ = 'j'
from src.login import Login
from src.main import WebmailTest
from src.config import Config


class Main:
    login = Login.Login()
    username = Config.USERNAME
    password = Config.PASSWORD
    def __init__(self):
        pass
    def fullCrawl(self):
        session = self.login.login(self.username, self.password)
        cookies = session.cookies
        w = WebmailTest.Webmail()
        w.crawl_url("https://webmail.hro.nl", cookies)



Main().fullCrawl()