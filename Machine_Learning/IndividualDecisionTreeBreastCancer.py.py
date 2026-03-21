import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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
# Step 4 : Create Model
#===========================================================================

model = DecisionTreeClassifier(random_state=42)

#===========================================================================
# Step 5 : Train Model
#===========================================================================

model.fit(X_train,Y_tarin)

#===========================================================================
# Step 6 : Test Model
#===========================================================================

y_pred = model.predict(X_test)

#===========================================================================
# Step 7 : Evalute the Model
#===========================================================================

print("Accuracy : ",accuracy_score(Y_test,y_pred)*100,"%")

print()

print("Confusion Matrix :")
print(confusion_matrix(Y_test,y_pred))

