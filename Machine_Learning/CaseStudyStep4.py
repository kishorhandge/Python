
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*80

#################################===============================###########################################
#                                    Step 1 : Load the dataset
#################################===============================###########################################

print()

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "iris (1).csv "

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")
print("Initial Entries from dataset : ")
print(df.head())    # display first 5 rows

print()

#################################================================###########################################
#                                  Step 2 : Data Analysis (EDA)
#################################================================###########################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of Dataset : ",df.shape)
print("Column Names :",list(df.columns))

print()

print("Missing Values (per column) :")
print(df.isnull().sum())

print()

print("Class Distribution (Species Count)")
print(df["species"].value_counts())

print()

print("Statistical Report of dataset :")
print(df.describe())

print()

#################################==========================================###########################################
#                                Step 3 : Decides independant and dependant variables
#################################===========================================###########################################

print(Border)
print("Step 3 : Decides independant and dependant variables")
print(Border)

# X : Independant varibales(features)
# Y : Dependant variballs (labels)

feature_cols = [

    "sepal length(cm)",
    "sepal width(cm)",
    "petal length(cm)",
    "petal width(cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

print()

#################################==========================================###########################################
#                                   Step 4 : Visualization of Dataset
#################################===========================================###########################################

print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)

print()

# Scatter plot

plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length(cm)"], temp["petal width(cm)"], label = sp)

plt.title("Iris : petal length vs petal width")

plt.xlabel("petal length(cm)")
plt.ylabel("petal width(cm)")

plt.legend()
plt.grid(True)
plt.show()

print()
