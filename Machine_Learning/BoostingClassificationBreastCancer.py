import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

#===========================================================================
# Step 1 : Load the dataset
#===========================================================================

df = pd.read_csv("Breast_Cancer.csv")
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
# Step 4 : Create bosting Model (Ada Boost)
#===========================================================================

boost_model = AdaBoostClassifier(
    n_estimators=50,
    random_state=42,
    learning_rate=1.0
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

print("Boosting Accuracy : ",accuracy_score(Y_test,y_pred)*100,"%")

print()

print("Confusion Matrix :")
print(confusion_matrix(Y_test,y_pred))

