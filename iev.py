#!/usr/bin/python

##Calculate expected offspring with dominant phenotype given parent pair numbers

from __future__ import division
import argparse

def main(parents):
    dom_prob={'AAAA':[1,int(parents[0])],'AAAa':[1,int(parents[1])],'AAaa':[1,int(parents[2])],'AaAa':[0.75,int(parents[3])],'Aaaa':[0.5,int(parents[4])],'aaaa':[0,int(parents[5])]}
    offsprings=0
    for key in dom_prob:
        offsprings+=dom_prob[key][0]*(2*dom_prob[key][1])
    return offsprings

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",metavar="Input file",required=True)
    args=parser.parse_args()
    with open(args.i,"r") as f:
        parents=f.readline().rstrip().split(" ")
        print main(parents)
