#!/usr/bin/env python3

''' Exercise 4 (spam detection)

In the src folder there are two files: "ham.txt.gz" and "spam.txt.gz".
The files are preprocessed versions of the files from
https://spamassassin.apache.org/old/publiccorpus/. There is one email
per line. The file ham.txt.gz contains emails that are non-spam, and,
conversely, emails in file spam.txt are spam. The email headers have
been removed, except for the subject line, and non-ascii characters
have been deleted.


Note. The tests use the fraction parameter with value 0.1 to ease to
load on the TMC server. If full data were used and the solution did
something non-optimal, it could use huge amounts of memory, causing
the solution to fail.
'''

import numpy as np
import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics

def spam_detection(random_state=0, fraction=0.01):
    # Read the lines from these files into arrays. Use function open from
    # gzip module, since the files are compressed. From each file take
    # only fraction of lines from the start of the file, where fraction is
    # a parameter to "spam_detection()", and should be in the range [0.0, 1.0].
    with gzip.open("src/ham.txt.gz", 'r') as f:
        ham = np.array(list(f))
    ham = ham[:int(fraction * len(ham))]

    with gzip.open("src/spam.txt.gz", 'r') as f:
        spam = np.array(list(f))
    spam = spam[:int(fraction*len(spam))]

    # use labels 0 for ham and 1 for spam
    X = np.concatenate((ham, spam))
    y = np.hstack(([0] * len(ham), [1] * len(spam)))

    # forms the combined feature matrix using CountVectorizer class’
    # fit_transform method. The feature matrix should first have the rows
    # for the ham dataset and then the rows for the spam dataset. One row
    # in the feature matrix corresponds to one email.
    cv = CountVectorizer()
    features = cv.fit_transform(X)

    # divide that feature matrix and the target label into training and
    # test sets, using train_test_split. Use 75% of the data for training.
    # Pass the random_state parameter from spam_detection to
    # train_test_split.
    Xtrain, Xtest, ytrain, ytest = train_test_split(features, y, random_state=random_state, train_size=0.75)

    # train a MultinomialNB model, and use it to predict the labels for the test set
    model = MultinomialNB()
    model.fit(Xtrain, ytrain)
    acc = metrics.accuracy_score(ytest, model.predict(Xtest))

    # The function should return a triple consisting of
    # * accuracy score of the prediction
    # * size of test sample
    # * number of misclassified sample points
    return acc, len(ytest), int((1-acc) * len(ytest))

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
