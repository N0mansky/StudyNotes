from queue import Queue, PriorityQueue
import threading


class Job(object):
    def __init__(self, prior, desc):
        self.prior = prior
        self.desc = desc
        print('New job:', desc)

    def __cmp__(self, other):
        return super.__cmp__(self.prior, other.prior)

    def __lt__(self,other):
        return self.prior < other.prior
    def __gt__(self,other):
        return self.prior > other.prior
    def __eq__(self,other):
        return self.prior < other.prior
    def __ne__(self,other):
        return self.prior != other.prior


q = PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))


def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.desc)
        q.task_done()


workers = [threading.Thread(target=process_job, args=(q,)),
           threading.Thread(target=process_job, args=(q,))]
for w in workers:
    w.setDaemon(True)
    w.start()

q.join()
