import sys        # for command line arguments
import os         # for file and folder operations
import time       # for time and scheduling delay
import schedule   # for automatic periodic execution
import shutil     # for copying files
import hashlib    # for generating file hash
import zipfile    # for creating zip archive


# ======================================================
# Function : Make_Zip
# Purpose  : Create zip archive of backup folder
# ======================================================
def Make_Zip(folder):

    # create timestamp for unique zip name
    timestamp = time.strftime("%Y-%M-%d_%H-%M-%S")

    # zip file name
    zip_name = folder + "_" + timestamp + ".zip"

    # open zip file in write mode with compression
    zobj = zipfile.ZipFile(zip_name ,'w',zipfile.ZIP_DEFLATED)

    # walk through all files inside folder
    for root ,dirs,files in os.walk(folder):
        for file in files:

            # full path of file
            full_path = os.path.join(root,file)

            # relative path for zip structure
            relative = os.path.relpath(full_path,folder)

            # add file into zip
            zobj.write(full_path,relative)

    # close zip file
    zobj.close()

    # return created zip name
    return zip_name


# ======================================================
# Function : Calculate_hash
# Purpose  : Generate MD5 hash of file
# Why      : Used to detect changed/duplicate files
# ======================================================
def Calculate_hash(path):
    
    # create md5 object
    hobj = hashlib.md5()

    # open file in binary mode
    fobj = open(path,"rb")

    # read file in chunks
    while True:
        data = fobj.read(1024)

        # stop when file ends
        if not data:
            break
        else:
            hobj.update(data)

    # close file
    fobj.close()

    # return hash value
    return hobj.hexdigest()


# =======================================================
# Function : BackUpFiles
# Purpose  : Copy only new/updated files to backup folder
# ======================================================
def BackUpFiles(Source,Destination):

    # list to store copied files
    Copied_Files = []

    print("Creating the backup folder for backup process")

    # create backup directory if not exists
    os.makedirs(Destination, exist_ok=True)

    # walk through source folder
    for root ,dirs,files in os.walk(Source):
        for file in files:

            # source file path
            src_path = os.path.join(root,file)

            # relative path
            relative = os.path.relpath(src_path,Source)

            # destination file path
            dest_path = os.path.join(Destination,relative)

            # create subfolders if needed
            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            # copy only if new file OR changed file
            if ((not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path))):
                
                shutil.copy2(src_path,dest_path)

                # store copied file name
                Copied_Files.append(relative)

    # return copied file list
    return Copied_Files
   

# ======================================================
# Function : MarvellousDataShieldStart
# Purpose  : Start full backup + zip process
# ======================================================
def MarvellousDataShieldStart(Source = "Data"):

    Border = "-"*50
    
    # backup folder name
    BackupName = "MarvellousBackup"

    print(Border)
    print("Backup Process Started Succesfully at :",time.ctime())
    print(Border)

    # copy files
    files = BackUpFiles(Source ,BackupName)

    # create zip archive
    zip_file = Make_Zip(BackupName)

    print(Border)
    print("Backup completed succesfully")
    print("Files copied :",len(files))
    print("Zip files gets created: ",zip_file)
    print(Border)


# ======================================================
# Function : main
# Purpose  : Control entire program flow
# ======================================================
def main():
     
    Border = "-"*50

    print(Border)
    print("-----------Marvellous Data Shield System----------")
    print(Border)
     
    # --------------------------------------------------
    # Case 1 : help option
    # --------------------------------------------------
    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to :")
            print("1 : Text Auto Backup At Given Time")
            print("2 : Backup only new and updated files")
            print("3 : Create An Archived of backup pereiodically")

        # --------------------------------------------------
        # Case 2 : usage option
        # --------------------------------------------------
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as")
            print("Script Name.py   Time Interval  SourceDirectory")
            print("Time Interval :  The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of Directory to backedup")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")


    # --------------------------------------------------
    # Case 3 : normal execution with interval + folder
    # Example : python demo.py 5 Data
    # --------------------------------------------------
    elif(len(sys.argv) == 3):

        print("Inside projects Logic")
        print("Time Interval :",sys.argv[1])
        print("Directory Name :",sys.argv[2])

        # schedule backup every X seconds
        schedule.every(int(sys.argv[1])).seconds.do(MarvellousDataShieldStart,sys.argv[2])

        print(Border)
        print("Data Shiled System Started Succesfully")
        print("Time Interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to Stop the execution")
        print(Border)

        # run scheduler continuously
        while True:
            schedule.run_pending()
            time.sleep(1)


    # --------------------------------------------------
    # Case 4 : invalid input
    # --------------------------------------------------
    else:
        print("Invalid Number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("---------Thank You For Using Our Script-----------")
    print(Border)


# ======================================================
# Entry Point
# ======================================================
if __name__ == "__main__":
    main()
