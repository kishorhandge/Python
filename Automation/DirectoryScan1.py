import os

def main():

    DirectoryName = input("Enter the name of directory : ")

    print("Contains of the directory are : ")

    for FolderName, SubFolderName ,FileName  in os.walk(DirectoryName):
        print("FolderName : ",FolderName)

        for Subf in SubFolderName:
            print("SubFolderName : ",Subf)

        for Fname in FileName:
            print("FileName : ",Fname)

if __name__ == "__main__":
    main()