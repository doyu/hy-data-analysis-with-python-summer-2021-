#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    c = Counter("abcdefghijklmnopqrstuvwxyzäö-")
    def f(w):
        for x in c:
            c[x] = 0
        c.update(Counter(w))
        assert len(c.values()) == 29, print(w) 
        return list(c.values())
    
    return np.array([f(w) for w in a])

def contains_valid_chars(s):
    for x in s:
        if not x in "abcdefghijklmnopqrstuvwxyzäö-":
            return False
    return True

def __get_features(l):
    l = list(map(lambda x: x.lower(), l))
    l = [w for w in l if contains_valid_chars(w)]
    X = get_features(l)
    return X

def get_features_and_labels():
    l = load_finnish()
    X1 = __get_features(l)
    y1 = np.array([0] * X1.shape[0])

    l = load_english()
    l  = [x for x in l if not x[0].isupper()]
    #l  = [x for x in l if not x.istitle()]
    X2 = __get_features(l)
    y2 = np.array([1] * X2.shape[0])

    X, y = np.concatenate([X1, X2]), np.concatenate([y1, y2])
    assert (X.shape[0] == 157006), f"X.shape[0]={X.shape[0]}"
    print(X1.shape, X2.shape)
    return X, y

def word_classification():
    X, y = get_features_and_labels()
    kf = KFold(n_splits=5, shuffle=True, random_state=0)
    return cross_val_score(MultinomialNB(), X, y, cv=kf)

def main():
    print(word_classification())

if __name__ == "__main__":
    main()
