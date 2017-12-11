#!/usr/bin/python

## Rosalind taking reverse complement of DNA string

import argparse
from string import maketrans

def main(dna):
	complement=maketrans("ACGT","TGCA")
	print dna.translate(complement)[::-1]

if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("-i",metavar="input file")
	args=parser.parse_args()
	with open (args.i,'r') as f:
		main(f.readline())
