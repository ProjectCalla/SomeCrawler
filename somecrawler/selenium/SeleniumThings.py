__author__ = 'j'


class JustSeleniumThings(object):
    display = None
    browser = None

    def __init__(self, display, browser):
        self.display = display
        self.browser = browser

    def stop(self):
        self.display.stop()
        self.browser.close()