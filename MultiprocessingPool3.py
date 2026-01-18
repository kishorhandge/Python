import time
import os

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

    for i in range(0,len(Data)):

        Ret = SumCube(Data[i])
        Result.append(Ret)

    end_time = time.time()

    print(Result)

    print("Total Execution time:",end_time - start_time)

if __name__ =="__main__":
    main()