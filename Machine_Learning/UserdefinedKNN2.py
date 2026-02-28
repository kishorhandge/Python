#   [A,B,C,D]
# X [1,2,3,5]
# Y [2,3,1,6]
#   [R R B B]

# predict(3,3) -> ?

import numpy as np
import math


def EucDistance(p1 ,p2):
    Ans = math.sqrt(((p1['X'] - p2['X']) ** 2) + (p1['Y']- p2['Y']) ** 2)

    return Ans
    
def MarvellousKNeighborsClassifier():

    Border = "-"*60

    Data = [
                {'point' : 'A', 'X' : 1, 'Y' : 2,'label' :'Red'},
                {'point' : 'B', 'X' : 2, 'Y' : 3,'label' :'Red'},
                {'point' : 'C', 'X' : 3, 'Y' : 1,'label' :'Blue'},
                {'point' : 'D', 'X' : 5, 'Y' : 6,'label' :'Blue'}
            
            ]
    
    print(Border)
    print("===============Marvellous User defined KNN==================")
    print(Border)

    print(Border)
    print("Training dataset")
    print(Border)

    for i in Data:
        print(i)


    print(Border)

    New_point = {'X': 3 ,'Y' : 3}

    print(Data[0])
    print(New_point)

    Result = EucDistance(Data[0],New_point)

    print(Result)

def main():
     
    MarvellousKNeighborsClassifier()

     

if __name__ == "__main__":
    main()