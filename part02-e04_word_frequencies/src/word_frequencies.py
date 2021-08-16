#!/usr/bin/env python3

'''
Exercise 4 (word frequencies)
Create function word_frequencies that gets a filename as a parameter and returns a dict with the word frequencies. In the dictionary the keys are the words and the corresponding values are the number of times that word occurred in the file specified by the function parameter. Read all the lines from the file and split the lines into words using the split() method. Further, remove punctuation from the ends of words using the strip("""!"#$%&'()*,-./:;?@[]_""") method call.

Test this function in the main function using the file alice.txt. In the output, there should be a word and its count per line separated by a tab:

The     64
Project 83
Gutenberg   26
EBook   3
of      303
'''

#d = {
#        "The":64,
#        "Project":83,
#        "Gutenberg":26,
#        "EBook":3,
#        "of":303
#    }

def word_frequencies(filename):
    d = dict()
    with open(filename, "r") as f:
        for line in f:
            l = line.split()
            for w in l:
                w = w.strip("""!"#$%&'()*,-./:;?@[]_""")
                if w in d:
                    d[w] = d[w] + 1
                else:
                    d[w] = 1
    return d

def main():
    d = word_frequencies("src/alice.txt")
    for k,v in d.items():
        print(f"{k}\t{v}")

if __name__ == "__main__":
    main()
