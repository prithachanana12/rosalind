#!/usr/bin/python

import argparse

def main(s,t):
	count=0
	for x in range(0,len(s)):
		if not s[x] == t[x]:
			count+=1
	print count


if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("-i",metavar="input file")
	args=parser.parse_args()
	with open (args.i,"r") as f:
		s=f.readline().rstrip("\n")
		t=f.next().rstrip("\n")
		main(s,t)
