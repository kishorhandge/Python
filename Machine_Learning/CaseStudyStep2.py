
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

Border = "-"*50

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
print(df.head())

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