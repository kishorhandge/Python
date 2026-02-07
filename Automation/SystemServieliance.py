
import psutil
import sys
import os
import time
import schedule


def CreateLog(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to creat folder")
            return
        
    
    else:
        os.mkdir(FolderName)
        print("Directory For Log Files Gets Created Succesfully")
    

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Logs file gets created ",FileName)

    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("------Marvellous Platform Serveilance System------"+"\n")
    fobj.write("Log Created At : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("--------------------- System Report -----------------\n")

    #print("Cpu Usage : ",psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n "%psutil.cpu_percent())
    fobj.write(Border+"\n")

    Mem = psutil.virtual_memory()

   # print("Ram Usage : ",Mem.percent)
    fobj.write("RAM Usage:  %s %%\n "%Mem.percent)
    fobj.write(Border+"\n")


    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            Usage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {Usage.percent}%%")
            fobj.write("%s -> %s %% used\n"%(part.mountpoint,Usage.percent))
        except:
            pass

    fobj.write(Border+"\n")

    net = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("sent : %.2f MB\n" % (net.bytes_sent / (1024*1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024*1024)))
    fobj.write(Border+"\n")


    fobj.write(Border+"\n")
    fobj.write("--------------End Of Log File-------------"+"\n")
    fobj.write(Border+"\n")


def ProcessScan():
    print("Process Scan Report")

    for proc in psutil.process_iter(attrs=["pid","name","status"]):
        info = proc.info
        print(info["pid"],info["name"],info["status"])

def main():
    ProcessScan()
    return

    Border = "-"*50
    print(Border)
    print("------Marvellous Platform Serveilance System------")
    print(Border)
     
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to :")
            print("1 : Create automatic logs")
            print("2 : Execute periodically")
            print("3 : Sends mails with the logs")  
            print("4 : Store infomation about processes")
            print("5 : Store infomation about cpu")
            print("6 : Store information about (RAM)Usage")
            print("7 : Store infomation about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as")
            print("Script Name.py   Time Interval  Directory Name")
            print("Time Interval :  The time in minutes for periodic scheduling ")
            print("Directory Name : Name of Directory to create auto logs")

        
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    #python demo.py 5 marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects Logic")
        print("Time Interval :",sys.argv[1])
        print("Directory Name :",sys.argv[2])

        #Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Serveilance System Started Succesfully")
        print("Directory Created With Name :",sys.argv[2])
        print("Time Interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to Stop the execution")


        #Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("---------Thank You For Using Our Script-----------")
    print(Border)

if __name__ == "__main__":
    main()

