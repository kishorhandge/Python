# ==========================================================
# Marvellous Platform Surveillance System
# This script creates system logs periodically
# Logs include CPU, RAM, Disk, Network and Process details
# ==========================================================

import psutil          # For system monitoring (CPU, RAM, processes)
import sys             # For command line arguments
import os              # For folder/file operations
import time            # For time and delays
import schedule        # For periodic task scheduling


# ==========================================================
# Function : CreateLog
# Creates folder + log file and writes full system report
# ==========================================================
def CreateLog(FolderName):

    Border = "-"*50     # Decorative border line

    Ret = False

    # Check if folder exists
    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        # If path exists but not directory
        if(Ret == False):
            print("Unable to creat folder")
            return
        
    else:
        # Create new folder
        os.mkdir(FolderName)
        print("Directory For Log Files Gets Created Succesfully")
    

    # Create timestamp based filename
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    print("Logs file gets created ",FileName)

    # Open file in write mode
    fobj = open(FileName,"w")


    # ---------- Header ----------
    fobj.write(Border+"\n")
    fobj.write("------Marvellous Platform Serveilance System------"+"\n")
    fobj.write("Log Created At : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("--------------------- System Report -----------------\n")


    # ---------- CPU Usage ----------
    fobj.write("CPU Usage : %s %%\n "%psutil.cpu_percent())
    fobj.write(Border+"\n")


    # ---------- RAM Usage ----------
    Mem = psutil.virtual_memory()
    fobj.write("RAM Usage:  %s %%\n "%Mem.percent)
    fobj.write(Border+"\n")


    # ---------- Disk Usage ----------
    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            Usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n"%(part.mountpoint,Usage.percent))
        except:
            pass

    fobj.write(Border+"\n")


    # ---------- Network Usage ----------
    net = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("sent : %.2f MB\n" % (net.bytes_sent / (1024*1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024*1024)))
    fobj.write(Border+"\n")


    # ---------- Process Log ----------
    data = ProcessScan()

    for info in data:
        fobj.write("pid :%s\n "%info.get("pid"))
        fobj.write("name :%s\n "%info.get("name"))
        fobj.write("username :%s\n "%info.get("username"))
        fobj.write("status :%s\n "%info.get("status"))
        fobj.write("start time :%s\n "%info.get("create_time"))
        fobj.write("cpu %% :%.2f\n "%info.get("cpu_percent"))
        fobj.write("memory %% :%.2f\n "%info.get("memory_percent"))
        fobj.write(Border+"\n")


    # ---------- Footer ----------
    fobj.write(Border+"\n")
    fobj.write("------------------End Of Log File-----------------"+"\n")
    fobj.write(Border+"\n")



# ==========================================================
# Function : ProcessScan
# Scans all running processes and returns their details
# ==========================================================
def ProcessScan():

    listprocess = []

    # Warm up CPU percent calculation
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)


    # Collect process information
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","username","status","create_time"])

            # Convert create time to readable format
            try:
                info["create_time"] = time.strftime("%Y-%M-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            listprocess.append(info)

        except (psutil.NoSuchProcess,psutil.AccessDenied ,psutil.ZombieProcess):
            pass
         
    return listprocess



# ==========================================================
# Main Function : Entry point of the program
# Handles command line arguments and scheduling
# ==========================================================
def main():
     
    Border = "-"*50                 # Decorative border line for output

    # Display program title
    print(Border)
    print("------Marvellous Platform Serveilance System------")
    print(Border)
     

    # ======================================================
    # Case 1 : Only 1 argument (Help or Usage)
    # ======================================================
    if(len(sys.argv) == 2):

        # Help option
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to :")
            print("1 : Create automatic logs")
            print("2 : Execute periodically")
            print("3 : Sends mails with the logs")  
            print("4 : Store infomation about processes")
            print("5 : Store infomation about cpu")
            print("6 : Store information about (RAM)Usage")
            print("7 : Store infomation about secondary storage")

        # Usage instructions option
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as")
            print("Script Name.py   Time Interval  Directory Name")
            print("Time Interval :  The time in minutes for periodic scheduling ")
            print("Directory Name : Name of Directory to create auto logs")

        
        # Invalid option
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")


    # ======================================================
    # Case 2 : Interval + Folder name provided
    # Example : python demo.py 5 marvellous
    # ======================================================
    elif(len(sys.argv) == 3):

        print("Inside projects Logic")
        print("Time Interval :",sys.argv[1])
        print("Directory Name :",sys.argv[2])

        # Apply scheduler to run CreateLog periodically
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Serveilance System Started Succesfully")
        print("Directory Created With Name :",sys.argv[2])
        print("Time Interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to Stop the execution")


        # Infinite loop to keep scheduler running
        while True:
            schedule.run_pending()   # Run scheduled task if time reached
            time.sleep(1)           # Wait 1 second to reduce CPU usage


    # ======================================================
    # Case 3 : Invalid number of arguments
    # ======================================================
    else:
        print("Invalid Number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")


    # Closing message
    print(Border)
    print("---------Thank You For Using Our Script-----------")
    print(Border)


# ==========================================================
# Program Entry Point
# Starts execution from here
# ==========================================================
if __name__ == "__main__":
    main()
