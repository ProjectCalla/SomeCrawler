__author__ = 'j'
class ConsumerJob():
    job_webmail = None
    job_osiris_personalia = None
    job_osiris_results = None
    job_osiris_credits = None
    job_mededelingen_phase_one = None
    job_mededelingen_phase_two = None

    def __init__(self, webmail=True, osiris_personalia=False, osiris_results=True, osiris_credits=True,
                 mededelingen_phase_one=False, mededelingen_phase_two=True):

        self.job_mededelingen_phase_one = mededelingen_phase_one
        self.job_mededelingen_phase_two = mededelingen_phase_two
        self.job_osiris_personalia = osiris_personalia
        self.job_osiris_credits = osiris_credits
        self.job_osiris_results = osiris_results
        self.job_webmail = webmail

    def startJob(self):
        if self.job_webmail:
            pass
        if self.job_osiris_personalia:
            pass
        if self.job_osiris_results:
            pass
        if self.job_osiris_credits:
            pass
        if self.job_mededelingen_phase_one:
            pass
        if self.job_mededelingen_phase_two:
            pass