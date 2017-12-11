#!/usr/bin/python

##Rosalind Count DNA Nucleotides

import argparse

def main(dna):
	print str(dna.count("A"))+" "+str(dna.count("C"))+" "+str(dna.count("G"))+" "+str(dna.count("T"))

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="counting nucleotides in a DNA string")
	parser.add_argument("-i",metavar="input file")
	args = parser.parse_args()
	f=open(args.i,'r')
	main(f.readline())
