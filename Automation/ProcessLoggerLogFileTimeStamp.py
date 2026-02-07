
import psutil
import sys
import os
import time


def CreateLog(FolderName):

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
    print(FileName)

    fobj = open(FileName,"w")
    

def main():

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

        CreateLog(sys.argv[2])


    else:
        print("Invalid Number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("---------Thank You For Using Our Script-----------")
    print(Border)

if __name__ == "__main__":
    main()