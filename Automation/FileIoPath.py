import os

def main():
    FileName = input("Enter the Name of file : ")

    Ret = os.path.isabs(FileName)

    if(Ret == True):
        print("It is Absolute path")
    
    else:
        print("It is Relative path")

       
if __name__ == "__main__":
    main()