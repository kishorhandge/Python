import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():

    #==============================================================================
    #   Step  1 : Load the dataset
    #==============================================================================

    print("Step 1 : Load the dataset\n")

    df = pd.read_csv("Mall_Customers.csv")

    print("First few records :")
    print(df.head())

    print("Shape of dataset :")
    print(df.shape)

    print("Missing values :")
    print(df.isnull().sum())

    #==============================================================================
    #   Step  2 : Select feautures (Independent)
    #==============================================================================

    print("Step 2 : Select feautures (Independent)")

    X = df[["AnnualIncome", "SpendingScore"]]
    print("Selected features :")
    print(X.head())

    print("shape of selected features :")
    print(X.shape)

    




if __name__ == "__main__":
    main()