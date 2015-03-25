__author__ = 'j'

from somecrawler.crawler.crawl import Webmail, OsirisPersonalia, AnnouncementsPhaseOne, OsirisCredits, OsirisResults
from somecrawler.job.BaseJob import BaseJob
import time
from somecrawler.memory.SharedObject import SharedObject

class ProducerJob(BaseJob):
    webmail_source = None
    osiris_results_source = None
    osiris_credits_source = None
    osiris_personalia_source = None
    announcements_phase_one_source = None
    announcements_phase_two_source = None

    def start(self):
        BaseJob.start(self)
        self.package_resources()


    def webmail(self, user, browser):
        print "Starting webmail"
        self.webmail_source = Webmail.WebmailProducer(self.user, browser).start()

    def osiris_results(self, user, browser):
        pass
        #self.osiris_results_source = OsirisResults.OsirisResultsProducer(self.user, browser).start()

    def osiris_personalia(self, user, browser):
        self.osiris_personalia_source = OsirisPersonalia.OsirisPersonaliaProducer(self.user, browser).start()

    def osiris_credits(self, user, browser):
        pass

    def announcements_phase_one(self, user, browser):
        pass
        #self.announcements_phase_one_source = AnnouncementsPhaseOne.AnnouncementsPhaseOneProducer(self.user, browser).start()

    def announcements_phase_two(self, user, browser):
        pass


    def package_resources(self):
        so = SharedObject(self.user, self.webmail_source, self.osiris_results_source, self.osiris_credits_source,
            self.osiris_personalia_source, self.announcements_phase_one_source, self.announcements_phase_two_source)

