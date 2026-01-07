#One Function Can Call Another Function

def fun():
    print("inside fun")

def gun():
    print("inside gun")
    fun()

def main():
    gun()
   

if __name__ == "__main__":
    main()
