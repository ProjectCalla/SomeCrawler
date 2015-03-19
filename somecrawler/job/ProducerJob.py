__author__ = 'j'

from somecrawler.crawler.crawl import Webmail, OsirisPersonalia, AnnouncementsPhaseOne, OsirisCredits, OsirisResults
from somecrawler.job.BaseJob import BaseJob
import time
from somecrawler.memory.SharedObject import SharedObject

class ProducerJob(BaseJob):

    def webmail(self, user):
        return Webmail.WebmailProducer(self.user).start()

    def osiris_results(self, user):
        return OsirisResults.OsirisResultsProducer(self.user).start()

    def osiris_personalia(self, user):
        return OsirisPersonalia.OsirisPersonaliaProducer(self.user).start()

    def osiris_credits(self, user):
        pass

    def announcements_phase_one(self, user):
        return AnnouncementsPhaseOne.AnnouncementsPhaseOneProducer(self.user).start()

    def announcements_phase_two(self, user):
        pass

    def add_to_shared_memory(self):
        resource = self.package_resources()
        #add to the shared memory

    def package_resources(self):
        return SharedObject(self.user, self.webmail_source, self.osiris_results_source, self.osiris_credits_source,
            self.osiris_personalia_source, self.announcements_phase_one_source, self.announcements_phase_two_source)
