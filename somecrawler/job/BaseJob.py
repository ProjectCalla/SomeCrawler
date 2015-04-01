__author__ = 'j'


class BaseJob():
    #To add an job at its var below, add it to the init and define own function
    thread_name = "BaseJob"

    job_configuration = None
    user = None
    priority = None

    #Handle browser better
    browser = None
    shared_object = None

    def __init__(self, user, shared_object=None):
        #General
        self.user = user
        self.job_configuration = user.job_configuration
        self.priority = user.priority
        self.shared_object = shared_object

    def start(self):
        if self.job_configuration.job_webmail:
            self.webmail_source = self.webmail()
        if self.job_configuration.job_osiris_personalia:
            self.osiris_personalia_source = self.osiris_personalia()
        if self.job_configuration.job_osiris_results:
            self.osiris_results_source = self.osiris_results()
        if self.job_configuration.job_osiris_credits:
            self.osiris_credits_source = self.osiris_credits()
        if self.job_configuration.job_announcements_phase_one:
            self.announcements_phase_one_source = self.announcements_phase_one()
        if self.job_configuration.job_announcements_phase_two:
            self.announcements_phase_two_source = self.announcements_phase_two()

    def webmail(self):
        raise Exception("Unimplemented abstract method: webmail()")
    def osiris_results(self):
        raise Exception("Unimplemented abstract method: osiris_results()")
    def osiris_personalia(self):
        raise Exception("Unimplemented abstract method: osiris_personalia()")
    def osiris_credits(self):
        raise Exception("Unimplemented abstract method: osiris_credits()")
    def announcements_phase_one(self):
        raise Exception("Unimplemented abstract method: announcements_phase_one()")
    def announcements_phase_two(self):
        raise Exception("Unimplemented abstract method: announcements_phase_two()")
