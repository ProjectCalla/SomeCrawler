__author__ = 'j'
from somecrawler.memory import SharedObject
from somecrawler.controller import SeleniumController as sel

class BaseJob():
    #To add an job at its var below, add it to the init and define own function
    thread_name = "BaseJob"
    job_webmail = None
    job_osiris_personalia = None
    job_osiris_results = None
    job_osiris_credits = None
    job_announcements_phase_one = None
    job_announcements_phase_two = None

    user = None
    priority = None

    #Handle browser better
    browser = None

    def __init__(self, user, webmail=True, osiris_personalia=False, osiris_results=True, osiris_credits=False,
                 announcements_phase_one=False, announcements_phase_two=False):
        #General
        self.user = user
        self.priority = user.priority
        #Jobs
        self.job_announcements_phase_one = announcements_phase_one
        self.job_announcements_phase_two = announcements_phase_two
        self.job_osiris_personalia = osiris_personalia
        self.job_osiris_credits = osiris_credits
        self.job_osiris_results = osiris_results
        self.job_webmail = webmail

    def start(self):
        self.browser = sel.login(sel.createBrowser(), self.user.username, self.user.password)
        if self.job_webmail:
            self.webmail_source = self.webmail(self.user, self.browser)
        if self.job_osiris_personalia:
            self.osiris_personalia_source = self.osiris_personalia(self.user, self.browser)
        if self.job_osiris_results:
            self.osiris_results_source = self.osiris_results(self.user, self.browser)
        if self.job_osiris_credits:
            self.osiris_credits_source = self.osiris_credits(self.user, self.browser)
        if self.job_announcements_phase_one:
            self.announcements_phase_one_source = self.announcements_phase_one(self.user, self.browser)
        if self.job_announcements_phase_two:
            self.announcements_phase_two_source = self.announcements_phase_two(self.user, self.browser)
        self.browser.close()

    def webmail(self, user, browser):
        raise Exception("Unimplemented abstract method: webmail()")
    def osiris_results(self, user, browser):
        raise Exception("Unimplemented abstract method: osiris_results()")
    def osiris_personalia(self, user, browser):
        raise Exception("Unimplemented abstract method: osiris_personalia()")
    def osiris_credits(self, user, browser):
        raise Exception("Unimplemented abstract method: osiris_credits()")
    def announcements_phase_one(self, user, browser):
        raise Exception("Unimplemented abstract method: announcements_phase_one()")
    def announcements_phase_two(self, user, browser):
        raise Exception("Unimplemented abstract method: announcements_phase_two()")
