
from sklearn import tree

# Rough - 1
# Smooth - 0

# Criceket - 2
# Tennis - 1


def main():

    print("Ball Classification Case Study")

    # Orignal Encoded DataSet
    # Independant Variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    # Dependant Vaariables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Independant Varibales for training
    Xtrain = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]

    # Independant Varibales for testing
    Xtest =  [[35,1],[95,0]]

    # Dependant Varibales for training
    Ytrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]

    # Dependant Varibales for testing
    Ytest =  [1,2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Xtrain,Ytrain)

    Result = trainedmodel.predict(Xtest) 

    print("Model predicts the object as : ",Result)


if __name__ == "__main__":
    main()

# Data Set Size : 15