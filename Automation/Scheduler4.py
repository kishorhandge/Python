import time
import datetime
import schedule

def Fun():
    print("Inside Fun at :",datetime.datetime.now())

def Gun():
    print("Inside Gun at :",datetime.datetime.now())

def main():
    print("Inside Marvellous Automation Script at :",datetime.datetime.now())

    #schedule.every(20).seconds.do(Fun)

    schedule.every(1).minute.do(Fun)

    schedule.every(1).hour.do(Gun)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()