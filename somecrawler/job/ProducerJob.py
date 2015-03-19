__author__ = 'j'

from somecrawler.crawler.crawl import Webmail, OsirisPersonalia, AnnouncementsPhaseOne, OsirisCredits, OsirisResults
from somecrawler.job.BaseJob import BaseJob
import time

class ProducerJob(BaseJob):

    def webmail(self, user):
        print Webmail.WebmailProducer(self.user).start()
        print "="*10+"\n"

    def osiris_results(self, user):
        print OsirisResults.OsirisResultsProducer(self.user).start()
        print "="*10+"\n"

    def osiris_personalia(self, user):
        print OsirisPersonalia.OsirisPersonaliaProducer(self.user).start()
        print "="*10+"\n"

    def osiris_credits(self, user):
        pass

    def announcements_phase_one(self, user):
        print AnnouncementsPhaseOne.AnnouncementsPhaseOneProducer(self.user).start()
        print "="*10+"\n"

    def announcements_phase_two(self, user):
        pass
