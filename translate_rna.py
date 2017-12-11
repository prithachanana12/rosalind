#!/usr/bin/python

import argparse
from Bio.Seq import translate

def main(rna_trans):
	print translate(rna_trans)

if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("-i",metavar="input file")
	args=parser.parse_args()
	with open (args.i,"r") as f:
		main(f.readline().rstrip('\n'))
