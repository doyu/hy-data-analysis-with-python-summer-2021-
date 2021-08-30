#!/usr/bin/env python3

'''Exercise 2 (plant classification)
Write function "plant_classification()" that does the following:

* loads the iris dataset using sklearn (sklearn.datasets.load_iris)
* splits the data into training and testing part using the
  train_test_split function so that the training set size is 80% of
  the whole data (give the call also the random_state=0 argument to
  make the result deterministic)
* use Gaussian naive Bayes to fit the training data
* predict labels of the test data
* the function should return the accuracy score of the prediction
  performance (sklearn.metrics.accuracy_score)
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    # * loads the iris dataset using sklearn (sklearn.datasets.load_iris)
    iris = load_iris()
    X = iris.data
    y = iris.target
    # * splits the data into training and testing part using the
    #   "train_test_split()" function so that the training set size is 80% of
    #   the whole data (give the call also the random_state=0 argument to
    #   make the result deterministic)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # * use Gaussian naive Bayes to fit the training data
    model = naive_bayes.GaussianNB()
    model.fit(X_train, y_train)

    # * predict labels of the test data
    y_predicted = model.predict(X_test)

    # * the function should return the accuracy score of the prediction
    #   performance (sklearn.metrics.accuracy_score)
    return metrics.accuracy_score(y_test, y_predicted)

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
