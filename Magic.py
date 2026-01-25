# dunder method / magic method / special method

class Demo:
    def __init__(self,A):
        self.No = A


obj1 = Demo(11)
obj2 = Demo(21)

print(11+21)        # 32
print(obj1 + obj2)  # TypeError: unsupported operand type(s) for +: 'Demo' and 'Demo'