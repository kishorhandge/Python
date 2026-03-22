from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

# Step 1 : Load the dataset

data = load_breast_cancer()

X = data.data
Y = data.target

print("Shape of X :",X.shape)
print("Shape of Y :",Y.shape)

# Step 2 : Split the dataset

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

# Step 3 : Create base models 

model_LR = LogisticRegression(max_iter=5000)
model_DT = DecisionTreeClassifier(random_state=42)
model_KNN = KNeighborsClassifier(n_neighbors=5)

# Step 4 : Train base models

model_LR.fit(X_train,Y_train)
model_DT.fit(X_train,Y_train)
model_KNN.fit(X_train,Y_train)

# Step 5 : Calculate Individual Accuracy

pred_LR = model_LR.predict(X_test)
pred_DT = model_LR.predict(X_test)
pred_KNN = model_LR.predict(X_test)

Acc_LR = accuracy_score(pred_LR,Y_test)
Acc_DT = accuracy_score(pred_DT,Y_test)
Acc_KNN = accuracy_score(pred_KNN,Y_test)

print("Individual model accuracy :")

print("Logistic Regression :",Acc_LR)
print("Decision Tree :",Acc_DT)
print("KNN :",Acc_KNN)


