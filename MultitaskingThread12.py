import threading
import time

def SumEven(No):
    sum = 0

    for i in range(2,No + 1,2):
        sum = sum + i
    
    print("Even Sum is:",sum)

def SumOdd(No):
    sum = 0

    for i in range(1,No + 1,2):
        sum = sum + i
    
    print("Odd Sum is:",sum)

def main():
    
    start_time = time.time()

    t1 = threading.Thread(target=SumEven,args=(10000000,))
    t2 = threading.Thread(target=SumOdd,args=(10000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()

    print("Time Required:",end_time - start_time)
    

if __name__ == "__main__":
    main()


