#!/usr/bin/python

##Rosalind transcribing DNA to RNA 

import argparse
from string import maketrans

def main(dna):
	myrna=maketrans("T","U")
	print dna.translate(myrna)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i",metavar="input file")
	args=parser.parse_args()
	with open(args.i,'r') as f:
		main(f.readline())
