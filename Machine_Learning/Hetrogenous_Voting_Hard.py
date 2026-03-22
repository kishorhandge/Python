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

# Step 5 : Hard Voting Classification

hard_model = VotingClassifier(

    estimators=[
        ('LR',model_LR),
        ('DT',model_DT),
        ('KNN',model_KNN)
    ],
    voting="hard"
)

hard_model.fit(X_train,Y_train)

pred_hard = hard_model.predict(X_test)

acc_hard = accuracy_score(pred_hard,Y_test)

print("Hard Voting Accuracy  :",acc_hard*100,"%")

