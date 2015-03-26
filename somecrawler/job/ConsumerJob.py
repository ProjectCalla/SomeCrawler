__author__ = 'j'

from somecrawler.crawler.crawl import Webmail, OsirisPersonalia, AnnouncementsPhaseOne, OsirisCredits, OsirisResults
from somecrawler.memory.SharedObject import SharedObject
from somecrawler.job.BaseJob import BaseJob
import time

class ConsumerJob(BaseJob):
    def start(self):
        if self.job_webmail:
            self.webmail_source = self.webmail()
        if self.job_osiris_personalia:
            self.osiris_personalia_source = self.osiris_personalia()
        if self.job_osiris_results:
            self.osiris_results_source = self.osiris_results()
        if self.job_osiris_credits:
            self.osiris_credits_source = self.osiris_credits()
        if self.job_announcements_phase_one:
            self.announcements_phase_one_source = self.announcements_phase_one()
        if self.job_announcements_phase_two:
            self.announcements_phase_two_source = self.announcements_phase_two()

    def webmail(self):
        Webmail.WebmailConsumer(self.shared_object.user, self.shared_object.webmail_source).start()
    def osiris_results(self):
        OsirisResults.OsirisResultsConsumer(self.shared_object.user, self.shared_object.osiris_results_source).start()
    def osiris_personalia(self):
        OsirisPersonalia.OsirisPersonaliaConsumer(self.shared_object.user, self.shared_object.osiris_personalia_source).start()
    def osiris_credits(self):
        pass
    def announcements_phase_one(self):
        AnnouncementsPhaseOne.AnnouncementsPhaseOneConsumer(self.shared_object.user, self.shared_object.announcements_phase_one_source).start()
    def announcements_phase_two(self):
        pass