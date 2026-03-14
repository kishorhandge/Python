import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix


#=====================================================================================
#
#   Function Name : LoadPreservedModel()
#   Description :   It is used to laod Model
#   Parameters :    filename
#   Return:         None
#   Date :          14-03-2026
#   Author :        Handge Kishor Surabhan
#
#=====================================================================================

def LoadPreservedModel(filename):

    loaded_model = joblib.load(filename)

    print("Model succesfully loaded :")

    return loaded_model


#=====================================================================================
#
#   Function Name : PreservedModel()
#   Description :   It is used to preserved model secondary
#   Parameters :    model,filename
#   Return:         None
#   Date :          14-03-2026
#   Author :        Handge Kishor Surabhan
#
#=====================================================================================

def PreservedModel(model,filename):
    joblib.dump(model,filename)

    print("Model preserved Succesfully with name :",filename)

#=====================================================================================
#
#   Function Name : Traintitanicmodel()
#   Description :   It does split,X,Y,training data,testing data
#   Parameters :    df
#   Return:         None
#   Date :          14-03-2026
#   Author :        Handge Kishor Surabhan
#
#=====================================================================================

def Traintitanicmodel(df):

    # Split the features and lable
    X = df.drop("Survived",axis = 1)
    Y = df["Survived"]

    print("\nFeatures :")
    print(X.head())

    print("\n Label")
    print(Y.head())

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

    print("X_train shape :",X_train.shape)
    print("X_test shape :",X_test.shape)
    print("Y_train shape :",Y_train.shape)
    print("Y_test shape :",Y_test.shape)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train,Y_train)

    print("model trained succesfully:")

    print("\n Intercept of model :")
    print(model.intercept_)

    print("\n Coefficinet of model :")
    for feature,coefficient in zip(X.columns , model.coef_[0]):
        print(feature , " : ",coefficient)


    PreservedModel(model,"Marvelloustitanic.pkl")

    loaded_model = LoadPreservedModel("Marvelloustitanic.pkl")

    y_pred = loaded_model.predict(X_test)

    accuracy = accuracy_score(y_pred,Y_test)

    print("Accuracy is :",accuracy)

    cm = confusion_matrix(y_pred,Y_test)

    print("Confusion matrix is :")
    print(cm)


#=====================================================================================
#
#   Function Name : DisplayInfo()
#   Description :   It display the formated title
#   Parameters :    title (str)
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
#   Function Name : CleanTitanicData()
#   Description :   It does preprocessing
#                   It removes unecesary columns
#                   It handles missing values
#                   It converts text data to numeric format
#                   It does encoding to categorical columns
#                   
#   Parameters :    df --> pandas dataframe
#   Return:         df -->Clean pandas datframe
#   Date :          14-03-2026
#   Author :        Handge Kishor Surabhan
#
#=====================================================================================

def CleanTitanicData(df):

    DisplayInfo("Step 2 : Orignal Data")
    print(df.head())

    # Remove Unnessary Column
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\n Columns to be droped")
    print(existing_columns)

    # Drop the unwanted columns
    df = df.drop(columns = existing_columns)

    DisplayInfo("Step 2 : Data After column removal")
    print(df.head())

    # Handle age column
    if "Age" in df.columns:
        print("Age column before filling missing value")
        print(df["Age"].head(10))


        # coerce-->Invalid value gets converted as NaN

        df["Age"] = pd.to_numeric(df["Age"],errors="coerce")

        age_median = df["Age"].median() 

        # Replace missing value with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge column after preprocessing :")
        print(df["Age"].head(10))

    # Handle Fare column
    if "Fare" in df.columns:

        print("\n Fare column before preprocessing")
        print(df["Fare"].head(10))

        fare_median = df["Fare"].median() 

        print("\n Median of Fare column is :",fare_median)

        # Replace missing value with median
        df["Fare"] = df["Fare"].fillna(fare_median)

        df["Fare"] = pd.to_numeric(df["Fare"],errors="coerce")

        print("\nFare column after preprocessing :")
        print(df["Fare"].head(10))


    # Handle Embarked column
    if "Embarked" in df.columns:

        print("\n Embarked column before preprocessing")
        print(df["Embarked"].head(10))

        # Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Remove missing values

        df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

        # get most frequenct value
        embarked_mode = df["Embarked"].mode()[0]
        print("Mode of Embarked column : ",embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked column after preprocessing :")
        print(df["Embarked"].head(10))


    # Handle sex column
     # Handle Fare column
    if "Sex" in df.columns:

        print("\n sex column before preprocessing")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"],errors="coerce")

        print("\nSex column after preprocessing :")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing")
    print(df.head())

    print("\nMissing value after preprocessing :")
    print(df.isnull().sum())

    # Encode Embarked column
   
    df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)
    print("\n Data after encoding")

    print(df.head())

    print("Shape of dataset :",df.shape)

    # Convert boolean columns into integer

    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\n Data after encoding")

    print(df.head())

    return df


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

    df = CleanTitanicData(df)

    Traintitanicmodel(df)


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