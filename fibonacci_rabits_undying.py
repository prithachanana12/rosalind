#!/usr/bin/python

##Rosalind Fibonacci rabbits

import argparse

def count_rabbits(a,b):
    my_list=[0,1,1]
    for i in range(3,a+1):
        my_list.append(int(my_list[i-1]) + (b*int(my_list[i-2])))
    return my_list[a]

def main(n,k):
    rabbits=count_rabbits(n,k)
    print rabbits

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n",metavar="number of months")
    parser.add_argument("-k",metavar="number of baby pairs in a litter")
    args=parser.parse_args()
    main(int(args.n),int(args.k))
