__author__ = 'j'
import re

title_regex = r"(\[\')(\\[n])(\s+)((\S+)\s(\S+))\2\s+\'\]"
node_digit = r"(\d+)"
unicode_list = r"\[\'(.+)\'\]"
webmail_header = r"(Name|Subject|Date|Size)"
embedded_report_unicode = r"\[u'(.+)'\]"
xao = r"\\xa0"

def mededelingenTitle(text):
    m = re.match(title_regex, text)
    if m:
        return m.group(4)

def getNodeNumbers(text):
    m = re.search(node_digit, text)
    if m:
        return m.group(1)
def filterListUnicode(text):
    m = re.search(unicode_list, text)
    if m:
        return m.group(1)
def filterWebmailHeader(text):
    m = re.search(webmail_header, text)
    if m:
        return re.sub(webmail_header, "", text)

def filterOsirisEmbeddedReportUnicode(text):
    r = None
    m = re.search(embedded_report_unicode, text)
    if m:
        return m.group(1)
    else:
        return text
def filterXao(text, replace):
    m = re.search(xao, text)
    if m:
        return re.sub(xao, replace, text)
    else:
        return text