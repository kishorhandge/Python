import os

def DirectoryScanner(DirectoryName = "Marvellous"):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such Directory")
        return
    

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("Unable to scan as its not a directory")
        return
    
    
    print("Contains of the directory are : ")

    for FolderName, SubFolderName ,FileName  in os.walk(DirectoryName):
        print("FolderName : ",FolderName)

        for Subf in SubFolderName:
            print("SubFolderName : ",Subf)

        for Fname in FileName:
            print("FileName : ",Fname)

def main():

    DirectoryName = input("Enter the name of directory : ")

    DirectoryScanner(DirectoryName)

if __name__ == "__main__":
    main()