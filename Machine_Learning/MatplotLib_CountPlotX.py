import matplotlib.pyplot as plt
import seaborn as sns

def main():

    sns.countplot(x = ["C","C","C++","JAVA","C++","PYTHON","JS","C++","GOLANG","C"] )

    plt.show()
    
if __name__ == "__main__":
    main()