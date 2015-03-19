__author__ = 'j'

from somecrawler.memory.SharedMemory import SharedMemory
from somecrawler.queue import QueueManager
from somecrawler.job import ConsumerJob, ProducerJob, JobController
from somecrawler.user import User
import thread
from somecrawler.exp import SomeThread
from somecrawler.threads import BaseThread, ThreadController
from somecrawler.queue import QueueManager

class TestMain:
    sharedMem = SharedMemory
    def __init__(self):
        pass
    def printUser(self, user):
        print user.username
        print user.priority

    def start(self):
        #Create queue
        #add all jobs
        #set producer threads
        #set consumer threads
        #Done

        jobs = JobController.create_producer_jobs_from_db()
        for i in range(len(jobs)):
            self.sharedMem.qManager.add_to_queue(self.sharedMem.pQueue, jobs[i], jobs[i].priority)


        threadCon = ThreadController.ThreadController()
        threadCon.spawn_producer_threads(5)
        for i in range(5):
            threadCon.producer_threads[i].start()



    def testJob(self):
        u = User.User("user", "password")
        job = ProducerJob.ProducerJob(u, webmail=True, osiris_personalia=True, osiris_results=True, osiris_credits=False,
                 announcements_phase_one=True, announcements_phase_two=False)
        job.start()
        pass


if __name__ == "__main__":
    TestMain().start()
    #TestMain().testJob()
    #TestMain().test2()