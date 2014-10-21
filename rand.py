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
    """Usage: {0} action [args]
    where action can be:
    n - random integer
    f - random file from current dir
    F - random file from current dir with full path
    """
    if (len(sys.argv) == 1):
        print >> sys.stderr, main.__doc__.format(os.path.basename(sys.argv[0]))
        return 1

    if (sys.argv[1] == "n"):
        try:
            val_min = int(sys.argv[2])
        except:
            print >> sys.stderr, "Usage: rand.py {max | min max}"
            return 1
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
