__author__ = 'j'
import ConsumerJob, ProducerJob
from somecrawler.user import UserController, User
from somecrawler.job.JobConfiguration import JobConfiguration

def create_producer_jobs_from_db():
    jobs = []
    users = UserController.UserController().getAllUsers()
    print users
    for i in range(len(users)):
        jobs.append(ProducerJob.ProducerJob(users[i]))
    return jobs

def create_consumer_jobs_from_db():
    jobs = []
    users = UserController.UserController().getAllUsers()
    for i in range(len(users)):
        jobs.append(ConsumerJob.ConsumerJob(users[i]))
    return jobs

def create_job(username, password, priority=5, webmail=True, osiris_personalia=False, osiris_results=True, osiris_credits=False,
                 announcements_phase_one=False, announcements_phase_two=False):
    return ConsumerJob.ConsumerJob(User.User(username, password, JobConfiguration(webmail, osiris_personalia,
                    osiris_results, osiris_credits, announcements_phase_one, announcements_phase_two)))

def print_jobDEBUG(jobs):
    for i in range(len(jobs)):
        print jobs[i].priority
        print jobs[i].user.username
        print jobs[i].user.password
        print jobs[i].__module__

def parse_producer_to_consumer(self):

    pass