import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#=====================================================================================
#
#   Function Name : DisplayInfo()
#   Description :   It display the formated title
#   Parameters :    title
#   Return:         None
#   Date :          14-03-2026
#   Author :        Handge Kishor Surabhan
#
#=====================================================================================


def DisplayInfo(title):

    print("\n"+"="*70)
    print(title)
    print("="*70)


#=====================================================================================
#
#   Function Name : ShowData()
#   Description   : It Shows basic information about datset
#   Parameters  :   (df)
#                   df --> pandas datframe object
#                   Message
#                   Message-->heading text display
#   Return:         None
#   Date :          14-03-2026
#   Author :        Handge Kishor Surabhan
#
#=====================================================================================

def ShowData(df,message):
    DisplayInfo(message)

    print("\nFirst Five rows of dataset")
    print(df.head())

    print("\nShape of dataset")
    print(df.shape)

    print("\nColumn names :")
    print(df.columns.tolist())

    print("\nMissing values of each column :")
    print(df.isnull().sum())


#=====================================================================================
#
#   Function Name : MarvellousTitanicLogistic()
#   Description :   This is main pipe controller
#                   It load the datset ,show raw data
#                   It preprocesses the datset and train the model
#   Parameters :    Datapath of dataset Pipe
#   Return:         None
#   Date :          14-03-2026
#   Author :        Handge Kishor Surabhan
#
#=====================================================================================

def MarvellousTitanicLogistic(Datapath):
    
    DisplayInfo("Step 1 : Loading the dataset")

    df = pd.read_csv(Datapath)

    ShowData(df,"Initial Dataset")


#=====================================================================================
#
#   Function Name : main()
#   Description :   Starting point of application
#   Parameters :    None
#   Return:         None
#   Date :          14-03-2026
#   Author :        Handge Kishor Surabhan
#
#=====================================================================================

def main():
    
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()