__author__ = 'j'
from somecrawler.crawler.crawl import Webmail, OsirisPersonalia, AnnouncementsPhaseOne

class ProducerJob:
    job_webmail = None
    job_osiris_personalia = None
    job_osiris_results = None
    job_osiris_credits = None
    job_mededelingen_phase_one = None
    job_mededelingen_phase_two = None
    start_job = False

    user = None
    #Create jobs from this?
    def __init__(self, user, webmail=True, osiris_personalia=False, osiris_results=True, osiris_credits=True,
                 mededelingen_phase_one=False, mededelingen_phase_two=True):
    #On default doesn't crawl the Personalia and Mededelingen Phase one
        self.user = user
        self.job_mededelingen_phase_one = mededelingen_phase_one
        self.job_mededelingen_phase_two = mededelingen_phase_two
        self.job_osiris_personalia = osiris_personalia
        self.job_osiris_credits = osiris_credits
        self.job_osiris_results = osiris_results
        self.job_webmail = webmail

    def startJob(self):
        if self.job_webmail:
            Webmail.WebmailProducer().start()
        if self.job_osiris_personalia:
            personalia = OsirisPersonalia.OsirisProducer().startPersonalia()
        if self.job_osiris_results:
            results = OsirisPersonalia.OsirisProducer().startResults()
        if self.job_osiris_credits:
            #?
            pass
        if self.job_mededelingen_phase_one:
            announcements = AnnouncementsPhaseOne.AnnouncementsPhaseOneProducer().start()
        if self.job_mededelingen_phase_two:
            #not implemented yet
            pass

    def start(self):
        pass