# -*- coding:utf-8 -*-
"""
DESC:\tCreating subprocesses each of which executes
multi thread tasks for data input to kinesis stream.
"""
__author__ = 'mitsu'
__status__ = 'test'
__version__ = '0.1'
__date__ = '24 Dec 2016'

import multiprocessing as mp
import time
import json
import myKinesisThread 
import boto3
## for test use ##
import os

def aSubProcess(queue, arrayOfRecords):
    """
    This function is executed in each sub process.
    In each sub process, multithreading function programmed
    in 'myKinesisThread' are triggered and the array of record
    data is passed.     
    
    @param arrayOfRecords: Array of record data which can be
    \t\tdecoded into JSON text.
    @return None
    """
    print("array: " + json.dumps(arrayOfRecords))
    myKinesisThread.multiThreading(arrayOfRecords)
    queue.put(0)

def mySubProcess(arrayOfRecords):
    """
    This function issues a sub process.
    The sub process possesses one recordArray 'arrayOfRecords'.
    Sub process program is defined in "aSubProcess".
    
    @param arrayOfRecords: Array of records data.
    @return None
    """    
    queue = mp.Queue()
    start = time.time()
    ps = mp.Process(target=aSubProcess, args=(queue, arrayOfRecords)) 
    ps.start()
    elapsed = time.time() - start
    print(("subProcess comsumed: {0}".format(elapsed)) + "\t[sec]")
    #print queue.get()
    ps.join()

def myMultiProcesses(delay, arrayOfRecordArrays):
    """
    This function issues number of multiprocess with time interval 'delay'.
    Each subprocess possesses a recordArray in 'arrayOfRecordArray'.
    Sub process program is defined in "aSubProcess".
    
    @param arrayOfRecordArray: Array of recordArray data.
    @return None
    """    
    queue = mp.Queue()
    numSubProcess = len(arrayOfRecordArrays)
    for j in range(0, numSubProcess):
        start = time.time()
        ps = mp.Process(target=aSubProcess, args=(queue, arrayOfRecordArrays[j])) 
        ps.start()
        time.sleep(delay)
        elapsed = time.time() - start
        print(("subProcess comsumed: {0}".format(elapsed)) + "\t[sec]")
        #print queue.get()
        ps.join()

if __name__ == "__main__":
    arr = []
    numThread = 40
    numSubProcess = 5
    for j in range(0,numSubProcess):
        test = []
        for i in range(0,numThread):
            num = i +  j * numThread
            test.append({"test" : str(num), "data": "aveve"})
        arr.append(test)
    myMultiProcessing(1, arr)
    #queue = mp.Queue()
    #for j in range(0, numSubProcess):
    #    start = time.time()
    #    ps = mp.Process(target=aSubProcess, args=(queue, arr[j])) 
    #    ps.start()
    #    time.sleep(1)
    #    elapsed = time.time() - start
    #    print(("subProcess comsumed: {0}".format(elapsed)) + "\t[sec]")
    #    #print queue.get()
    #    ps.join()

