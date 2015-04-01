__author__ = 'j'

from somecrawler.memory import SharedMemoryManager
from somecrawler.job import ProducerJob, JobController, JobConfiguration
from somecrawler.user import User
from somecrawler.threads import ThreadController
from somecrawler.config import Config
import yappi


class TestMain:
    queue = SharedMemoryManager.queue

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
            self.queue.add_to_queue(self.queue.pQueue, jobs[i], jobs[i].priority)

        thread_con = ThreadController.ThreadController()

        thread_con.spawn_producer_threads(Config.PRODUCER_THREADS)
        for i in range(Config.PRODUCER_THREADS):
            thread_con.producer_threads[i].start()

#//==================   Consumer
        thread_con.spawn_consumer_threads(Config.CONSUMER_THREADS)
        for i in range(Config.CONSUMER_THREADS):
            thread_con.consumer_threads[i].start()


#//==================   Join threads
        for i in range(Config.PRODUCER_THREADS):
            thread_con.producer_threads[i].join()

        for i in range(Config.CONSUMER_THREADS):
            thread_con.consumer_threads[i].join()

        yappi.get_func_stats().print_all()

    def testJob(self):
        yappi.start()
        u = User.User("user", "pass", JobConfiguration.JobConfiguration())
        job = ProducerJob.ProducerJob(u)
        job.start()
        yappi.get_func_stats().print_all()


    def yetAnotherTest(self):
        u = User.User("user", "pass", JobConfiguration.JobConfiguration(webmail=False, osiris_personalia=True))
        ProducerJob.ProducerJob(u).start()

    def sanity_checks(self):
        #Check for internet
        #Check OS
        pass
if __name__ == "__main__":
    TestMain().start()
    #TestMain().testJob()
    #TestMain().test2()

    #TestMain().yetAnotherTest()
