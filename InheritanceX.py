class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
        self.No1 = 10
        self.No2 = 20

    def Fun(self):
        print("Inside Fun method of Parent",self.No1,self.No2)

class Child(Parent):
    def __init__(self):
        super().__init__()
        
        print("Inside Child Constructor")
        self.A = 11
        self.B = 21

    def Sun(self):
        print("Inside Sun method Of Child",self.A,self.B,self.No1,self.No2)

cobj = Child()

print(cobj.No1) # 10
print(cobj.No2) # 20

print(cobj.A)   # 11
print(cobj.B)   # 21

cobj.Fun()
cobj.Sun()

