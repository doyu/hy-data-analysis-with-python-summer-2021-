#!/usr/bin/env python3

import pandas as pd

def read_series():
    serie = pd.Series([], dtype='object')
    line = input()
    value_list = []
    index_list = []
    while line != "":
        try:
            line = line.split()
            value = line[1]
            index = line[0]
            index_list.append(index)
            value_list.append(value)
        except:
            print("Error")
        line = input()
    serie2 = pd.Series(value_list, index = index_list)
    return serie.append(serie2)

def main():
    print(read_series())

if __name__ == "__main__":
    main()
