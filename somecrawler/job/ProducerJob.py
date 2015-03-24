__author__ = 'j'

from somecrawler.crawler.crawl import Webmail, OsirisPersonalia, AnnouncementsPhaseOne, OsirisCredits, OsirisResults
from somecrawler.job.BaseJob import BaseJob
import time
from somecrawler.memory.SharedObject import SharedObject

class ProducerJob(BaseJob):

    def webmail(self, user, browser):
        print "Starting webmail"
        return Webmail.WebmailProducer(self.user, browser).start()

    def osiris_results(self, user, browser):
        #return OsirisResults.OsirisResultsProducer(self.user, browser).start()
        pass
    def osiris_personalia(self, user, browser):
        #return OsirisPersonalia.OsirisPersonaliaProducer(self.user, browser).start()
        pass
    def osiris_credits(self, user, browser):
        pass

    def announcements_phase_one(self, user, browser):
        #return AnnouncementsPhaseOne.AnnouncementsPhaseOneProducer(self.user, browser).start()
        pass
    def announcements_phase_two(self, user, browser):
        pass

    def add_to_shared_memory(self):
        resource = self.package_resources()
        #add to the shared memory

    def package_resources(self):
        return SharedObject(self.user, self.webmail_source, self.osiris_results_source, self.osiris_credits_source,
            self.osiris_personalia_source, self.announcements_phase_one_source, self.announcements_phase_two_source)
