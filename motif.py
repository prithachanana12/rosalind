#!/usr/bin/python

import argparse
import re

def main(s,t):
	print [(m.start()+1) for m in re.finditer('(?={0})'.format(t),s)]
	

if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("-i",metavar="input file")
	args=parser.parse_args()
	with open (args.i,"r") as f:
		s=f.readline().rstrip('\n')
		t=f.next().rstrip('\n')
		main(s,t)
