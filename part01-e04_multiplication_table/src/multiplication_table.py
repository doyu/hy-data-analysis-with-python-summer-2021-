#!/usr/bin/env python3

import numpy as np

def main():
    [print(("{:4d}"*10).format(*l)) for l in [(np.array(range(1,11)) * n) for n in range(1,11)]]

if __name__ == "__main__":
    main()
