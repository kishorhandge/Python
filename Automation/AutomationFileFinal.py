import hashlib
import os
import time
import schedule
import sys


def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while (len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):

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
    
    Duplicate = {}  # dict

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):

        for Fname in FileName:
            Fname = os.path.join(FolderName,Fname)  #use to combine folder path and file name
            CheckSum = CalculateCheckSum(Fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(Fname)

            else:
                Duplicate[CheckSum] = [Fname]

    return Duplicate

def DisplayResult(MyDict):

    Result = list(filter(lambda x : len(x) > 1 ,MyDict.values()))

    Count = 0

    for value in Result:
        for subvalue in value:
            Count+=1
            print(subvalue)

        print("Value of Count is : ",Count)
        Count = 0

def DeleteDuplicate(path = "Marvellous"):
    MyDict = FindDuplicate(path)
    
    Result = list(filter(lambda x : len(x) > 1 ,MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count+=1
            if(Count > 1):
                print("Deleted File : ",subvalue)
                os.remove(subvalue)
                Cnt+=1

        Count = 0

    print("Total deleted files : ",Cnt)    

# ======================================================
# Main Function
# ======================================================
def main():

    Border = "-"*50                 # Decorative border line

    # Display program title
    print(Border)
    print("----------Marvellous Directory Automation---------")
    print(Border)


    # ======================================================
    # Case 1 : Only 1 argument (Help or Usage)
    # ======================================================
    if(len(sys.argv) == 2):

        # Help option
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to :")
            print("1 : Scan directory periodically")
            print("2 : Automate directory monitoring")
            print("3 : Execute tasks using scheduler")

        # Usage option
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the script as :")
            print("ScriptName.py   DirectoryName")
            print("DirectoryName : Name of directory to scan")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")


    # ======================================================
    # Case 2 : Directory name provided
    # Example : python demo.py TestFolder
    # ======================================================
    elif(len(sys.argv) == 2):

        print("Inside Directory Automation Logic")
        print("Directory Name :", sys.argv[1])

        # Apply scheduler
        schedule.every(1).minutes.do(DeleteDuplicate, sys.argv[1])

        print("Directory Automation Started Successfully")
        print("Press Ctrl + C to Stop the execution")

        # Infinite loop
        while True:
            schedule.run_pending()
            time.sleep(1)


    # ======================================================
    # Case 3 : Invalid arguments
    # ======================================================
    else:
        print("Invalid Number of command line arguments")
        print("Unable to proceed")
        print("Please use --h or --u to get more details")


    # Closing message
    print(Border)
    print("---------Thank You For Using Our Script-----------")
    print(Border)


# ======================================================
# Program Entry Point
# ======================================================
if __name__ == "__main__":
    main()