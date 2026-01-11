No = 11     #global

def  fun():
    No = 21     #local
    print("Value of No from fun is :",No)   #21
    

print("Value of No is :",No)    #11
fun()