__author__ = 'j'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from src.config import Config
import time

class Webmail:
    def __init__(self):
        pass

    def correct_url(self, url):
     if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
     return url

    def scrollDown(self, browser, numberOfScrollDowns):
        body = browser.find_element_by_tag_name("body")
        while numberOfScrollDowns >=0:
            body.send_keys(Keys.PAGE_DOWN)
            numberOfScrollDowns -= 1
        return browser

    def crawl_url(self, url, cookies, run_headless=True):
        if run_headless:
            display = Display(visible=0, size=(1024, 768))
            display.start()

        #Initialize browser
        browser = webdriver.Firefox()
        browser.get(self.correct_url(url))
        cookies
        #Start crawl
        self.login(browser)
        browser = self.scrollDown(browser, 10)

        # all_hover_elements = browser.find_elements_by_class_name("hover-box")
        #
        # for hover_element in all_hover_elements:
        #     a_element = hover_element.find_element_by_tag_name("a")
        #     product_title = a_element.get_attribute("title")
        #     product_link = a_element.get_attribute("href")
        # print product_title, product_link

        browser.quit()

    def login(self, browser):
        body = browser.find_element_by_tag_name("body")
        print body
        #return browser on login