
from sklearn.datasets import load_iris

def main():

    print("Iris Classification Case Study :")

    Dataset = load_iris()

    # Meta data of dataset
    print("Independant Varibales are : ")
    print(Dataset.feature_names)
    print("Length of Independant Varibales is :",len(Dataset.feature_names))

    print("Dependant Variables are : ")
    print(Dataset.target_names)
    print("Length of dependant Varibales is :",len(Dataset.target_names))


if __name__ == "__main__":
    main()


