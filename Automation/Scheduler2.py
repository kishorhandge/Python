import time
import datetime
import schedule

def Fun():
    print("Inside Fun at :",datetime.datetime.now())

def main():
    print("Inside Marvellous Automation Script at :",datetime.datetime.now())

    schedule.every(20).seconds.do(Fun)
    
# Problem
if __name__ == "__main__":
    main()