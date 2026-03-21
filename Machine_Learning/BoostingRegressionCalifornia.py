import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error,r2_score


#===========================================================================
# Step 1 : Load the dataset
#===========================================================================

df = pd.read_csv("California_Housing.csv")
print("Shape of datset :",df.shape)
print("First 5 records : ",df.head())

#===========================================================================
# Step 2 : Seperate features and Labels
#===========================================================================

X = df.drop("target",axis=1)

Y = df["target"]

#===========================================================================
# Step 3 : Split the dataset for training and testing
#===========================================================================

X_train,X_test,Y_tarin,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)


#===========================================================================
# Step 4 : Create Gradient boosting Model
#===========================================================================

boost_model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
    )

#===========================================================================
# Step 5 : Train Boosting Model
#===========================================================================

boost_model.fit(X_train,Y_tarin)

#===========================================================================
# Step 6 : Test Boosting Model
#===========================================================================

y_pred = boost_model.predict(X_test)

#===========================================================================
# Step 7 : Evalute the Boosting Model
#===========================================================================

print("Mean_Squared_Error :",mean_squared_error(Y_test,y_pred))
print("R_Square :",r2_score(Y_test,y_pred))

