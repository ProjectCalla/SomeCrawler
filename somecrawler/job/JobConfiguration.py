__author__ = 'j'

class JobConfiguration(object):
    job_announcements_phase_one = None
    job_announcements_phase_two = None
    job_osiris_personalia = None
    job_osiris_credits = None
    job_osiris_results = None
    job_webmail = None

    def __init__(self, webmail=True, osiris_personalia=False, osiris_results=True, osiris_credits=False,
                 announcements_phase_one=False, announcements_phase_two=False):

        self.job_announcements_phase_one = announcements_phase_one
        self.job_announcements_phase_two = announcements_phase_two
        self.job_osiris_personalia = osiris_personalia
        self.job_osiris_credits = osiris_credits
        self.job_osiris_results = osiris_results
        self.job_webmail = webmail
