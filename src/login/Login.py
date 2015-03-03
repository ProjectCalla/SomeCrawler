__author__ = 'j'
import requests
from lxml import etree
class Login:

    def __init__(self):
        pass
    def login(self, username, password):
        print "trying to log in"
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        payload = {
                "username" : username,
                "password" : password

                   }
        #First get login info
        req = session.get('https://hint.hro.nl')

        #adds the payload that is generated to log in
        payload[str(etree.HTML(req.text).xpath('//*[@id="formwrap"]/form/div/input[1]/@name')).replace("[\'", "").replace("\']", "")] = ltVal = str(etree.HTML(req.text).xpath('//*[@id="formwrap"]/form/div/input[1]/@value')).replace("[\'", "").replace("\']", "")
        payload[str(etree.HTML(req.text).xpath('//*[@id="formwrap"]/form/div/input[2]/@name')).replace("[\'", "").replace("\']", "")] = str(etree.HTML(req.text).xpath('//*[@id="formwrap"]/form/div/input[2]/@value')).replace("[\'", "").replace("\']", "")
        payload[str(etree.HTML(req.text).xpath('//*[@id="formwrap"]/form/div/input[3]/@value')).replace("[\'", "").replace("\']", "")] = str(etree.HTML(req.text).xpath('//*[@id="formwrap"]/form/div/input[3]/@value')).replace("[\'", "").replace("\']", "")

        #login
        req = session.post('https://login.hro.nl/v1/login?service=http%3a%2f%2fhint.hro.nl%2fDefault.aspx%3fid%3d37184%26epslanguage%3dnl&allow=mcr-nt-upt', data=payload)
        return session