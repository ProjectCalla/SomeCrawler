__author__ = 'j'

from somecrawler.memory import SharedMemoryManager
from somecrawler.queue import QueueManager
from somecrawler.job import ConsumerJob, ProducerJob, JobController
from somecrawler.user import User
import thread, time
from somecrawler.exp import SomeThread
from somecrawler.threads import BaseThread, ThreadController
from somecrawler.queue import QueueManager
import yappi

class TestMain:
    shared_mem_producer = SharedMemoryManager.producer
    shared_mem_consumer = SharedMemoryManager.consumer

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
#//===================   Producer
        print "creating queue, may take a while..."
        jobs = JobController.create_producer_jobs_from_db()
        for i in range(len(jobs)):
            self.shared_mem_producer.qManager.add_to_queue(self.shared_mem_producer.pQueue, jobs[i], jobs[i].priority)

        producer_threads = 10
        thread_con = ThreadController.ThreadController()
        thread_con.spawn_producer_threads(producer_threads)
        for i in range(producer_threads):
            thread_con.producer_threads[i].start()

        for i in range(producer_threads):
            thread_con.producer_threads[i].join()
#//==================   Consumer

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