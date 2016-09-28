# python3
import sys, threading
from datetime import datetime
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class JobQueue():
    def __init__(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        for i in range(len(self.jobs)):
            next_worker = 0
            print('iteration n ' + str(i))
            for j in range(self.num_workers):
                print('iteration workers ' + str(j))
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]
            print(str(self.assigned_workers[i]), self.start_times[i])

    def make_work(self, jobtime, currentWorker):
        #print(str(currentWorker))
        print(currentWorker, self.start_time)
        #self.start_time = + jobtime
        return

    def new_implement(self):
        for i in range(len(self.jobs)):
            for j in range(self.num_workers):
                self.make_work(self.jobs[i], j)

    def solve(self):
        self.assign_jobs()
        #self.new_implement()


def main():
    tstart = datetime.now()
    job_queue = JobQueue()
    job_queue.solve()
    tend = datetime.now()
    print(tend - tstart)

threading.Thread(target=main).start()