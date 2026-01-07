def  EmployeeInfo(Name,Age,Salary,City):
    print("Name :",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)

def main():
    #Positional
    #EmployeeInfo("Aryan",21,1000.50,"Beed")     #Correct
    #EmployeeInfo(26,"Aryan","Beed",1000.50)     #Wrong

    #Keyword
    EmployeeInfo(Age = 26,Name = "Aryan",City = "Beed",Salary = 1000.50)        #Correct

if __name__ == "__main__":
    main()