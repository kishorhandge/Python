# python CommandLine5.py 11 21

import sys

def main():
    if(len(sys.argv) < 3 or len(sys.argv) > 3):
        print("Invalid Number of arguments")
    else:

        No1 = int(sys.argv[1])
        No2 = int(sys.argv[2])

        print(No1 + No2)
    

if __name__ == "__main__":
    main()
    