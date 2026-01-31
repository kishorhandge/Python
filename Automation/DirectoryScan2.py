import os

def DirectoryScanner(DirectoryName):

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