# -*- coding:utf-8 -*-
"""
DESC:\tThreading a process and executing
record puts based on input JSON data
"""
__author__ = 'mitsu'
__status__ = 'test'
__version__ = '0.1'
__date__ = '24 Dec 2016'

import threading
import time
import boto3
import json
import os

_log_ = "threads.log"
LOCK = threading.Lock()

def thread(_data):
    """
    Executing a record put in thread towards kinesis stream.
    This function is internally triggered by 'multiThreading' function.

    @param _data: JSON data which is to put into kinesis stream after json decoding
    @return None
    """
    with LOCK:
        client = boto3.client('kinesis')
    try:
        #print(json.dumps(_testDat))
        response = client.put_record(
            StreamName = "testKinesisStream",
            Data = json.dumps(_data),
            PartitionKey = '222')
    except Exception, e:
        with LOCK:
            fo = open(_log_, "a")
            try:
                fo.write(str(Exception) + "\n" + str(_data) + "\n" +
                         str(response) + "\n\n")
            except:
                fo.write(str(Exception) + "\n" + str(_data) + "\n\n")
            fo.close()


def multiThreading(data):
    """
    This function executes a number of thread task according to the input
    data, which is the array of JSON data. The number of threads equals to
    the number of JSON data in the array.
    
    @param data: Array of JSON data.
    @return None
    """
    #print("begins threading")
    thArr = []
    for i in range(0, len(data)):
        thArr.append(threading.Thread(target=thread, args=(data[i],)))
        thArr[i].start()
    for i in range(0, len(data)):
        thArr[i].join()

if __name__ == "__main__":
    arr = []
    for i in range(0,3):
        arr.append({"test": i, "data": "uweuwe"})
    multiThreading(arr)
