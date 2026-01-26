# python CommandLine4.py 11 21 

import sys

def main():

    # print("Command Line Arguments are: ")
    
    # for i in range(len(sys.argv)):
        
        # print(int(sys.argv[1]) + int(sys.argv[2]))

    No1 = int(sys.argv[1])
    No2 = int(sys.argv[2])

    print(No1 + No2)

if __name__ == "__main__":
    main()