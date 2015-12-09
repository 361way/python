#!/usr/bin/env python
## DATE: 2011-01-20
## FILE: queue.py
## WEBSITE: http://themattreid.com
from Queue import *
from threading import Thread, Lock

'''this function will process the items in the queue, in serial'''
def processor():
    if queue.empty() == True:
        print "the Queue is empty!"
        sys.exit(1)
    try:
        job = queue.get()
        print "I'm operating on job item: %s"%(job)
        queue.task_done()
    except:
        print "Failed to operate on job"

'''set variables'''
queue = Queue()
threads = 4
    
'''a list of job items. you would want this to be more advanced,
like reading from a file or database'''
jobs = [ "job1", "job2", "job3" ]

'''iterate over jobs and put each into the queue in sequence'''
#for job in jobs:
for job in range(100):
     print "inserting job into the queue: %s"%(job)
     queue.put(job)

'''start some threads, each one will process one job from the queue'''
for i in range(threads):
     th = Thread(target=processor)
     th.setDaemon(True)
     th.start()

'''wait until all jobs are processed before quitting'''
queue.join() 
