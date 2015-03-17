__author__ = 'j'
WEBMAIL_FRAME = '//*[@id="idWebAccFrameset"]/frame[2]'
WEBMAIL_EMAIL_INFO = '//*[@id="msglist"]/div[1]/div/table/tbody/tr[{0}]/td[{1}]/text()'

OSIRIS_PERSONALIA_MAIN = '//*[@id="form0"]/table/tbody/tr/td/table[5]/tbody/tr[2]/td[2]/table[1]/tbody/tr/td[2]/table/tbody/tr[{0}]/td[{1}]/span/text()'
OSIRIS_PERSONALIA_GROUP = '//*[@id="StudentgroepPerStudent"]/table[2]/tbody/tr[{0}]/td/span/text()'

OSIRIS_RESULTS_MAIN = '//*[@id="ResultatenPerStudent"]/table/tbody/tr/td/table/tbody/tr[{0}]/td[{1}]/span/text()'

MEDEDELINGEN_PHASE_ONE_TEXT = '//*[@id="{0}"]/div[2]/div/div/ul/li[{1}]/@class'
MEDEDELINGEN_PHASE_ONE_TITLE = '//*[@id="{0}"]/div[2]/div/div/ul/li[{1}]/h4/text()'
MEDEDELINGEN_PHASE_ONE_HEADER = '//*[@id="{0}"]/div[1]/h3/span[1]/text()'