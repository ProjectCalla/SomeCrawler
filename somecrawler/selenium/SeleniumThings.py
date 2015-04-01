__author__ = 'j'


class JustSeleniumThings(object):
    display = None
    browser = None

    def __init__(self, display, browser):
        self.display = display
        self.browser = browser

    def stop(self):
        try:
            self.display.stop()
            #After browser.close() it tries to make a connection with a TCP socket, no idea why.
            self.browser.close()
        except:
            print "Couldn't close.."