import hashlib
import os

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while (len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):

    Ret = False

    Ret = os.path.exists(DirectoryName)
    
    if(Ret == False):
        print("There is no such directory")
        return
    

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):

        for Fname in FileName:
            Fname = os.path.join(FolderName,Fname)
            CheckSum = CalculateCheckSum(Fname)


            print(f"File Name : {Fname} CheckSum : {CheckSum}")


def main():
     
    DirectoryWatcher()


if __name__ == "__main__":
    main()