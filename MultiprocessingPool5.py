import os
import multiprocessing
import time

def SumCube(No):
    print("process is running with PID :",os.getpid())
    
    sum = 0

    for i in range(1,No + 1):
        sum = sum +(i**3)  #change

    return sum

def main():

    Data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,1000000]

    Result = []         # Result = list()

    start_time = time.time()

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumCube,Data)

    pobj.close()
    pobj.join()

    end_time = time.time()

    print(Result)

    print("Total Execution time:",end_time - start_time)

if __name__ =="__main__":
    main()