import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousAdvertise(datapath):

    Border = "-"*60
    #========================================================================================
    # Step 1 : Load dataset
    #========================================================================================

    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)

    df = pd.read_csv(datapath)

    print("Few records from dataset  : ")
    print(df.head())

    #========================================================================================
    # Step 2 : Remove unwanted columns
    #========================================================================================

    print(Border)
    print("Step 2 : Remove unwanted columns ")
    print(Border)

    print("Shape of dataset before removal :",df.shape)

    if "Unnamed: 0" in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)


    print("Shape of dataset after removal :",df.shape)

    print(Border)
    print("Clean dataset is :")
    print(Border)

    print(df.head())


    #========================================================================================
    # Step 3 : Check missing values
    #========================================================================================

    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Missing values Count :\n",df.isnull().sum())

    #========================================================================================
    # Step 4 : Display Statistical Summary
    #========================================================================================

    print(Border)
    print("Step 4 : Display Statistical Summary")
    print(Border)

    print(df.describe())

    #========================================================================================
    # Step 5 : Correlation between columns
    #========================================================================================

    print(Border)
    print("Step 5 : Correlation between columns")
    print(Border)

    print("Correlation matrix")
    print(df.corr())

    #========================================================================================
    # Step 6 : Split dataset into Independent and Dependent Variables 
    #========================================================================================

    print(Border)
    print("Step 6 : Split dataset into Independent and Dependent Variables ")
    print(Border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of Independent Varibales :",X.shape)
    print("Shape of Dependent Varibales :",Y.shape)

    #========================================================================================
    # Step 7 : Split the dataset for training and testing 
    #========================================================================================

    print(Border)
    print("Step 7 : Split the dataset for training and testing ")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    
    print("X_train shape :",X_train.shape)
    print("X_test shape :",X_test.shape)
    print("Y_train shape :",Y_train.shape)
    print("Y_test shape :",Y_test.shape)

    #========================================================================================
    # Step 8 : Create and train the model 
    #========================================================================================

    print(Border)
    print("Step 8 : Create and train the model ")
    print(Border)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    #========================================================================================
    # Step 9 : Test the model 
    #========================================================================================

    print(Border)
    print("Step 9 : Test the model ")
    print(Border)

    y_pred = model.predict(X_test)

    #========================================================================================
    # Step 10 : Evaluate the model 
    #========================================================================================

    print(Border)
    print("Step 10 : Evaluate the model ")
    print(Border)

    MSE = mean_squared_error(Y_test,y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test,y_pred)

    print("Mean Squared error :",MSE)
    print("Root Mean Squared error :",RMSE)
    print("R sqaure value :",R2)

    #========================================================================================
    # Step 11 : Calculate model coefficient 
    #========================================================================================

    print(Border)
    print("Step 11 : Calculate model coefficient ")
    print(Border)

    for column , value in zip(X.columns,model.coef_):
        print(f"{column} : {value}")

    print("Intercept : ",model.intercept_)

    #========================================================================================
    # Step 12 : Compare the Actual and Predicted values 
    #========================================================================================

    print(Border)
    print("Step 12 : Compare the Actual and Predicted values ")
    print(Border)

    result = pd.DataFrame({'Actual sale ':Y_test.values,
                           'Predicted sale ':y_pred})
    

    print(result.head())

    #========================================================================================
    # Step 13 : Plot Actual VS Predicted 
    #========================================================================================

    print(Border)
    print("Step 13 : Plot Actual VS Predicted ")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,y_pred)

    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")

    plt.title("Actual sales VS Predicted sales")

    plt.grid(True)

    plt.show()


def main():

    MarvellousAdvertise("Advertising.csv")


if __name__ == "__main__":
    main()