
def phoenix():
    print("inside phoenix")

    def zara():
        print("inside zara")

def main():
    phoenix.zara()
   
if __name__ == "__main__":
    main()
