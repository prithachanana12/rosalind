#!/usr/bin/python

##Rosalind GC content compute

from __future__ import division
import argparse

def fasta(filename):
    seqs={}
    with open (filename,'r') as fasta:
        for line in fasta:
            if line.startswith('>'):
                name=line.rstrip('\n')
                seqs[name]=''
            else:
                seqs[name]+=line.rstrip('\n')
    return seqs
    

def main(filename):
    gc_per=0
    sequences=fasta(filename)
    for key in sequences:
        g=sequences[key].rstrip('\n').count('G')
        c=sequences[key].rstrip('\n').count('C')
        gc=((g+c)/len(sequences[key].rstrip('\n')))*100
        if (gc > gc_per):
            gc_per = gc
            seq=str(key)
        return (seq.strip('>'),("%.6f" % gc_per))

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",metavar="input fasta",required=True)
    args=parser.parse_args()
    foo,bar=main(args.i)
    print foo
    print bar

