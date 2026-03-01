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

    print("X_mean is : ",mean_X)    
    print("Y_mean is : ",mean_Y)


def main():

    MarvellousPredictor()

if __name__ == "__main__":
    main()

