
import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile

def Make_Zip(folder):
    timestamp = time.strftime("%Y-%M-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    # open the zip file

    zobj = zipfile.ZipFile(zip_name ,'w',zipfile.ZIP_DEFLATED)

    for root ,dirs,files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)

    zobj.close()

    return zip_name

def Calculate_hash(path):
    
    hobj = hashlib.md5()

    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()


def BackUpFiles(Source,Destination):
    Copied_Files = []

    print("Creating the backup folder for backup process")

    os.makedirs(Destination, exist_ok=True) #if folder exists don't give me a error go ahead

    for root ,dirs,files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            # Copy the files if it is new
            if ((not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path))):
                
                shutil.copy2(src_path,dest_path)
                Copied_Files.append(relative)

    return Copied_Files
   

def MarvellousDataShieldStart(Source = "Data"):
    Border = "-"*50
    
    BackupName = "MarvellousBackup"

    print(Border)
    print("Backup Process Started Succesfully at :",time.ctime())
    print(Border)

    files = BackUpFiles(Source ,BackupName)

    zip_file = Make_Zip(BackupName)

    print(Border)
    print("Backup completed succesfully")
    print("Files copied :",len(files))
    print("Zip files gets created: ",zip_file)
    print(Border)

def main():
     

    Border = "-"*50
    print(Border)
    print("-----------Marvellous Data Shield System----------")
    print(Border)
     
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to :")
            print("1 : Text Auto Backup At Given Time")
            print("2 : Backup only new and updated files")
            print("3 : Create An Archived of backup pereiodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as")
            print("Script Name.py   Time Interval  SourceDirectory")
            print("Time Interval :  The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of Directory to backedup")

        
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    #python demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects Logic")
        print("Time Interval :",sys.argv[1])
        print("Directory Name :",sys.argv[2])

        #Apply the scheduler
        schedule.every(int(sys.argv[1])).seconds.do(MarvellousDataShieldStart,sys.argv[2])

        print(Border)
        print("Data Shiled System Started Succesfully")
        print("Time Interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to Stop the execution")
        print(Border)

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

