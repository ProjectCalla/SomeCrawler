__author__ = 'j'

from somecrawler.crawler.crawl import Webmail, OsirisPersonalia, AnnouncementsPhaseOne, OsirisCredits, OsirisResults
from somecrawler.job.BaseJob import BaseJob
import time

class ProducerJob(BaseJob):

    def webmail(self, user):
        Webmail.WebmailProducer(self.user).start()

    def osiris_results(self, user):
        OsirisResults.OsirisResultsProducer(self.user).start()

    def osiris_personalia(self, user):
        OsirisPersonalia.OsirisPersonaliaProducer(self.user).start()

    def osiris_credits(self, user):
        pass

    def announcements_phase_one(self, user):
        AnnouncementsPhaseOne.AnnouncementsPhaseOneProducer().start()

    def announcements_phase_two(self, user):
        pass
