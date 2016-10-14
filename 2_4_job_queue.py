# python3
# ************  Description: ***************
# program takes two arguments on first line, first is number of workers,
# second - workers treads, next line represent each tread working time
# Each worker take tread and work given amount of time, output the worker and start time of each job in line,
# Workers can't do more than one job in one time
# Example:
# 2 5
# 1 2 3 4 5
# Output:
# 0 0 #First worker take first job at time 0 and work it 1 sec
# 1 0 #Second worker take second job at time 0 and work it 2 sec
# 0 1 #First worker already done first job, take job number 3 at time 1, and do it 3 sec
# 1 2 #Second worker take job number 4 at time 2 and do it 4 sec
# 0 4 #First worker take last job at time 4

import sys, threading
import heapq
from datetime import datetime
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class JobQueue():
    def __init__(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        #assert m == len(self.jobs)
        #self.assigned_workers = [None] * len(self.jobs)
        #self.start_times = [None] * len(self.jobs)
        self.next_free_time = [0] * self.num_workers # Worker countdown
        self.worker = 0

    def new_implement(self):
        i = 0
        for j in self.jobs:
            current_time = self.next_free_time[self.worker]
            if i > current_time or i == 0:
                print(str(self.worker) + ' ' + str(current_time))
                self.next_free_time[self.worker] = current_time + self.jobs[i]
                self.worker += 1
                if self.worker > self.num_workers - 1:
                    self.worker = 0
            else:
                # Take closet worker to process
                closest_item = min(self.next_free_time)
                self.worker = self.next_free_time.index(closest_item)
                print(str(self.worker) + ' ' + str(closest_item))
                self.next_free_time[self.worker] += self.jobs[i]
            i += 1
            #print(str(self.next_free_time))

    def solve(self):
        self.new_implement()

		
#if __name__ == "__main__":
def main():
    #tstart = datetime.now()
    job_queue = JobQueue()
    job_queue.solve()
    #tend = datetime.now()
    #print(tend - tstart)

threading.Thread(target=main).start()