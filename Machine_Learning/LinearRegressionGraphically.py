import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():
    # Load the Data

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independant varibales : X -",X)
    print("Values of dependant varibales : Y -",Y)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("X_mean is : ",mean_X)    # 3.0
    print("Y_mean is : ",mean_Y)    # 3.6

    n = len(X)  # 5

    # Y = mX + C 

    # m = (sumamation (X-X_bar) * (Y- Y_bar)) / (summation ((X-X_bar) ** 2))

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_X) * (Y[i] - mean_Y))
        denominator = denominator + ((X[i] - mean_X) ** 2)


    m = numerator / denominator

    print("Slope of line i.e : m  = ",m) # 0.4

    C = mean_Y - (m * mean_X) # Y = mX + c

    print("Y intercept of line i.e c : ",C) # 2.4

    x = np.linspace(1,6,n)
    y = C + m * x

    plt.plot(x,y,color = 'g',label = "Regression Line")
    plt.scatter(X,Y,color = 'r',label = "Scatter Plot")

    plt.xlabel("X : Independent Varibale")
    plt.ylabel("Y : Dependent Varibale")

    plt.legend()

    plt.show()

    # find ?
    # yp
    # R^2



def main():

    MarvellousPredictor()

if __name__ == "__main__":
    main()

