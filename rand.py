#!/usr/bin/python2

import random
import sys
import os


def random_file(full_path):
    if (full_path):
        return os.path.join(os.getcwd(),
                            random.choice(os.listdir(os.getcwd())))
    else:
        return random.choice(os.listdir(os.getcwd()))


def random_number(val_min, val_max):
    if (val_max == 0):
        return random.randint(val_max, val_min)
    else:
        return random.randint(val_min, val_max)


def main():
    if (sys.argv[1] == "n"):
        try:
            val_min = int(sys.argv[2])
        except:
            print "Use: rand.py [min] [max]"
            sys.exit(1)
        try:
            val_max = int(sys.argv[3])
        except:
            val_max = 0
        print random_number(val_min, val_max)
    elif (sys.argv[1] == "f"):
        print random_file(False)
    elif (sys.argv[1] == "F"):
        print random_file(True)
    else:
        print "Unknown command"


if __name__ == "__main__":
    sys.exit(main())
