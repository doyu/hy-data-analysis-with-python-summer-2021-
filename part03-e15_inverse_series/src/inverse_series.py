#!/usr/bin/env python3

'''
Exercise 15 (inverse series)
Write function inverse_series that get a Series as a parameter and
returns a new series, whose indices and values have swapped roles.
Test your function from the main function.

What happens if some value appears multiple times in the original
Series? What happens if you use this value to index the resulting
Series?

One may notice that there are similarities between Python’s
dictionaries and Pandas’ Series, both can be thought to access values
using keys. The difference is that Series requires that the indices
have all the same type, and similarly, all the values have the same
type. This restriction allows creation of fast data structures.

As a mark of the similaries between these two data structures, Pandas
allows creation of a Series object from a dictionary:


[24]:
d = { 2001 : "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017 : "Trump"}
s4 = pd.Series(d, name="Presidents")
s4
[24]:
2001     Bush
2005     Bush
2009    Obama
2013    Obama
2017    Trump
Name: Presidents, dtype: object

'''

import pandas as pd

def inverse_series(s):
#    print(s.index)
#    print(s.values)
    return pd.Series(s.index, index=s.values)

def main():
    print(inverse_series(pd.Series([1,2,3],index=list("abc"))))
    return

if __name__ == "__main__":
    main()
