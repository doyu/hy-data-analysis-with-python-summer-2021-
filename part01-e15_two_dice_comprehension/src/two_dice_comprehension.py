#!/usr/bin/env python3

def main():
    L = [(x, y)
         for y in range(1,7)
         for x in range(1,7)
         if (x + y == 5)]
    for x in L:
        print(x)

if __name__ == "__main__":
    main()
