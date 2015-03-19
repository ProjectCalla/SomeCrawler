__author__ = 'j'

class SharedObject():
    user = None
    announcements_phase_one_source = None
    announcements_phase_two_source = None
    osiris_personalia_source = None
    osiris_credits_source = None
    osiris_results_source = None
    webmail_source = None

    def __init__(self, user, announcements_phase_one_source=None, announcements_phase_two_source=None,
                 osiris_personalia_source=None, osiris_credits_source=None, osiris_results_source=None,
                 webmail_source=None):

        self.user = user
        self.announcements_phase_one_source = announcements_phase_one_source
        self.announcements_phase_two_source = announcements_phase_two_source
        self.osiris_personalia_source = osiris_personalia_source
        self.osiris_credits_source = osiris_credits_source
        self.osiris_results_source = osiris_results_source
        self.webmail_source = webmail_source
