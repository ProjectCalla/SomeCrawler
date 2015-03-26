__author__ = 'j'

from somecrawler.crawler.crawl import Webmail, OsirisPersonalia, AnnouncementsPhaseOne, OsirisCredits, OsirisResults
from somecrawler.job.BaseJob import BaseJob
from somecrawler.job.ConsumerJob import ConsumerJob

import time
from somecrawler.memory.SharedObject import SharedObject
from somecrawler.memory import SharedMemoryManager
from somecrawler.controller import SeleniumController as sel

class ProducerJob(BaseJob):
    webmail_source = None
    osiris_results_source = None
    osiris_credits_source = None
    osiris_personalia_source = None
    announcements_phase_one_source = None
    announcements_phase_two_source = None
    shared_memory = SharedMemoryManager.shared

    def start(self):
        #Executes all the functions below, see BaseJob class
        self.browser = sel.login(sel.createBrowser(), self.user.username, self.user.password)
        BaseJob.start(self)
        self.browser.close()
        self.add_to_shared_memory()

    def webmail(self):
        print "Starting webmail"
        return Webmail.WebmailProducer(self.user, self.browser).start()

    def osiris_results(self):
        pass
        #self.osiris_results_source = OsirisResults.OsirisResultsProducer(self.user, self.browser).start()
    def osiris_personalia(self):
        pass
        #self.osiris_personalia_source = OsirisPersonalia.OsirisPersonaliaProducer(self.user, self.browser).start()
    def osiris_credits(self):
        pass
    def announcements_phase_one(self):
        pass
        #self.announcements_phase_one_source = AnnouncementsPhaseOne.AnnouncementsPhaseOneProducer(self.user, self.browser).start()
    def announcements_phase_two(self):
        pass

    def add_to_shared_memory(self):
        print "Adding to shared memory"
        job = self.create_consumer_job()
        self.shared_memory.qManager.add_to_queue(self.shared_memory.pQueue, job, job.priority)

    def package_resources(self):
        so = SharedObject(self.user, announcements_phase_one_source=self.announcements_phase_one_source,
                          announcements_phase_two_source=self.announcements_phase_two_source,
                          osiris_personalia_source=self.osiris_personalia_source,
                          osiris_credits_source=self.osiris_credits_source,
                          osiris_results_source=self.osiris_results_source, webmail_source=self.webmail_source)
        return so

    def create_consumer_job(self):
        so = self.package_resources()
        self.print_soDEBUG(so)
        return ConsumerJob(self.user, webmail=self.job_webmail, osiris_personalia=self.job_osiris_personalia,
            osiris_results=self.job_osiris_results, osiris_credits=self.job_osiris_credits,
            announcements_phase_one=self.job_announcements_phase_one,
            announcements_phase_two=self.job_announcements_phase_two, shared_object=so)

    def print_soDEBUG(self,so):
        if so.announcements_phase_one_source != None:
             print "announcements_phase_one_source = not null"
        else:
            print "announcements_phase_one_source = null"
        if so.announcements_phase_two_source != None:
            print "announcements_phase_two_source = not null"
        else:
            print "announcements_phase_two_source = null"
        if so.osiris_credits_source != None:
            print "osiris_credits_source = not null"
        else:
            print "osiris_credits_source = not null"
        if so.osiris_personalia_source != None:
            print "osiris_personalia_source = not null"
        else:
            print "osiris_personalia_source = null"
        if so.user != None:
            print "user = not null"
        else:
            print "user = null"
        if so.webmail_source != None:
            print "Webmail_source = Not null"
        else:
            print "Webmail_source = null"