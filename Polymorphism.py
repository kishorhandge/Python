class Parent:
    def __init__(self):
        print("Inside Parent Constructor")

    def Fun(self):
        print("Inside Fun method of Parent")

class Child(Parent):
    def __init__(self):  
        super().__init__()
        print("Inside Child Constructor")

    def Fun(self):
        super().Fun()
        print("Inside Fun method Of Child")

cobj = Child()

cobj.Fun()

 

