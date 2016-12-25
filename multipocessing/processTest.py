import multiprocessing as mp
import time
import json
import myKinesisThread 
import boto3
## for test use ##
import os

def aSubProcess(queue, arr):
    print("arr:" + json.dumps(arr))
    myKinesisThread.multiThreading(arr)
    queue.put(0)


if __name__ == "__main__":
    arr = []
    numThread = 40
    numSubProcess = 5
    for j in range(0,numSubProcess):
        test = []
        for i in range(0,numThread):
            num = i +  j * numThread
            test.append({"test" : str(num)})
        arr.append(test)
    queue = mp.Queue()
    for j in range(0, numSubProcess):
        start = time.time()
        ps = mp.Process(target=aSubProcess, args=(queue, arr[j])) 
        ps.start()
        time.sleep(1)
        elapsed = time.time() - start
        print(("subProcess comsumed: {0}".format(elapsed)) + "\t[sec]")
        print queue.get()
        ps.join()

