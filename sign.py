#!/usr/bin/python
##Enumerating oriented gene orderings

import argparse
import itertools

def main(n,filename):
    f=open(filename,'w+')
    #f.write("\n"+"\n")
    tot=0
    l=range(-n,0)
    l.extend(range(1,n+1))
    combs=list(itertools.permutations(l,n))
    for i in range (0,len(combs)):
        a=list(combs[i])
        if len([abs(num) for num in a]) == len(set([abs(num) for num in a])):
            tot+=1
            f.write(str(a).strip("[").strip("]").replace(",","")+"\n")
    f.seek(0)
    s=f.read()
    f.close()
    with open(filename,'w+') as f2:
        f2.write(str(tot)+"\n"+s)
    f2.close()
    

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-n",metavar="positive integer indicating length of permutations",required=True)
    parser.add_argument("-o",metavar="path to output file",required=True)
    args=parser.parse_args()
    main(int(args.n),args.o)
