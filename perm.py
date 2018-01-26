#!/usr/bin/python

##Calculate permutations of the given list

import itertools
import argparse

def main(n):
    a=1
    for i in range(1,n+1):
        a*=i
    print a
    perms = list(itertools.permutations(range(1,n+1)))
    for i in range(0,len(perms)):
        print str(perms[i]).strip("()").replace(",", "")

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-n",metavar="positive integer",required=True)
    args=parser.parse_args()
    main(int(args.n))

