#!/usr/bin/python

##Compute probability of getting a dominant phenotype offspring acc to Mendel's first law

from __future__ import division
import argparse

def main(dom,het,res):
    total=dom+het+res
    p_res=(res/total)*((res-1)/(total-1))
    p_het=((het/total)*((het-1)/(total-1)))*(1/4)
    p_both=(((het/total)*(res/(total-1)))+((res/total)*(het/(total-1))))*(1/2)
    p_dom=1-(p_res+p_het+p_both)
    return ("%.6f" % p_dom)

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",metavar="input file",required=True)
    args=parser.parse_args()
    with open(args.i,"r") as f:
        a,b,c=f.readline().split()
        print main(int(a),int(b),int(c))
