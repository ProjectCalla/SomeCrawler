__author__ = 'j'

from somecrawler.memory.SharedMemory import SharedMemory
from somecrawler.queue import QueueManager
from somecrawler.job import ConsumerJob, ProducerJob, JobController
from somecrawler.user import User
import thread, time
from somecrawler.exp import SomeThread
from somecrawler.threads import BaseThread, ThreadController
from somecrawler.queue import QueueManager
import yappi

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
        yappi.start()
        ##!!Producer only!!
        print "creating queue, may take a while..."
        jobs = JobController.create_producer_jobs_from_db()
        for i in range(len(jobs)):
            self.sharedMem.qManager.add_to_queue(self.sharedMem.pQueue, jobs[i], jobs[i].priority)

        threads = 10
        threadCon = ThreadController.ThreadController()
        threadCon.spawn_producer_threads(threads)
        for i in range(threads):
            #threadCon.producer_threads[i].daemon = True
            threadCon.producer_threads[i].start()

        # while self.sharedMem.pQueue.counter != 0:
        #     "Sleeping ZzZz.."
        #     time.sleep(1)

        for i in range(threads):
            threadCon.producer_threads[i].join()

        yappi.get_func_stats().print_all()

    def testJob(self):
        yappi.start()
        u = User.User("user", "pass")
        job = ProducerJob.ProducerJob(u, webmail=True, osiris_personalia=True, osiris_results=True, osiris_credits=False,
                 announcements_phase_one=True, announcements_phase_two=False)
        job.start()
        yappi.get_func_stats().print_all()



if __name__ == "__main__":
    TestMain().start()
    #TestMain().testJob()
    #TestMain().test2()