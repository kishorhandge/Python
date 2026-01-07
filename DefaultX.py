def  EmployeeInfo(Name="golya",Age=27,Salary =1000.50,City="Pune"):
    print("Name :",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)

def main():
    EmployeeInfo("Aryan", 26,1000.50)        #Correct
    EmployeeInfo("Aryan", 26,1000.50,"Beed")         
     
    
if __name__ == "__main__":
    main()