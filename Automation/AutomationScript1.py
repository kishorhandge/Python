import sys

def main():
    Border = "_"*40
    print(Border)
    print("--------- Marvellous Automation --------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to Perform _______")
            print("This is a Automation Script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Used the given Script as")
            print("ScriptName.py Argumet1 Argument2")
            print("Argument1 : ____________")
            print("Argument2 : ____________")

        else:
            print("Parameter Not Matched")
            print("Used the given flags as: ")
            print("__u : Used to display the usage")
            print("__h : Used to display the help")

    else:
        print("Invalid Number of Command Line Arguments")
        print("Used the given flags as: ")
        print("__u : Used to display the usage")
        print("__h : Used to display the help")

    print(Border)
    print("-----Thank You For Using Our Script-----")
    print("--------- Marvellous Infosystems -------")
    print(Border)


if __name__ == "__main__":
    main()