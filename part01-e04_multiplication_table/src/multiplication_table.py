#!/usr/bin/env python3


def main():
    pass
    for y in range(1, 11):
        for x in range(1, 11):
            if x == 10:
                c = '\n'
            else:
                c = ''
            print('{:4d}'.format(x*y), end=c)

if __name__ == "__main__":
    main()
