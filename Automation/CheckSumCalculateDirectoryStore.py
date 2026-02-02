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

def FindDuplicate(DirectoryName = "Marvellous"):

    Ret = False

    Ret = os.path.exists(DirectoryName)
    
    if(Ret == False):
        print("There is no such directory")
        return
    

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):

        for Fname in FileName:
            Fname = os.path.join(FolderName,Fname)
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

def main():
     
    DeleteDuplicate()

if __name__ == "__main__":
    main()