#!/usr/bin/python2

import random
import sys

def main():
    try:
	min = int(sys.argv[1])
	#print min
	try:
	    max = int(sys.argv[2])
	except Exception:
	    print random.randint(0, min)
	    sys.exit(0)
	print random.randint(min, max)
    except IndexError:
	print "Use: rand.py [min] [max]"


if __name__ == "__main__":
    sys.exit(main())
