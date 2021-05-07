#!/usr/bin/env python3

from lex_tokens import *
from parse_tokens import *
import argparse

def main(s):
	token_list = tokenize(s)
	res = parsing(token_list)[0]
	print(res)
	


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Json Parser")
	parser.add_argument("-f", "--file", help="[+] file name")
	parser.add_argument("-s", "--string", help="[+] enter string")
	args = parser.parse_args()
	if args.file:
		try:
			f = open(args.file,'r').read()
			main(f)
		except:
			raise Exception("File not Found")
	elif args.string:
		main(args.string)
	else:
		raise Exception("Invalid Arguments use -h")