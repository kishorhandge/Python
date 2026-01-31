import os

def main():
    FileName = input("Enter the Name of file : ")

    if(os.path.exists(FileName)):

        Ret = os.path.isabs(FileName)

        if(Ret == True):
            print("It is Absolute path")
        
        else:
            print("It is Relative path")
            NewPath = os.path.abspath(FileName)

            print("Updated path : ",NewPath)

    else:
        print("There is no such file")
       
if __name__ == "__main__":
    main()