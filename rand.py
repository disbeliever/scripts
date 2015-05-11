#!/usr/bin/python3

import random
import sys
import os


def random_file(full_path):
    files = os.listdir(os.getcwd())
    if (len(files) > 0):
        if (full_path):
            return os.path.join(os.getcwd(),
                                random.choice(files))
        else:
            return random.choice(os.listdir(files))
    else:
        return ""


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
        print (main.__doc__.format(os.path.basename(sys.argv[0])), file=sys.stderr)
        return 1

    if (sys.argv[1] == "n"):
        try:
            val_min = int(sys.argv[2])
        except:
            print ("Usage: rand.py {max | min max}", file=sys.stderr)
            return 1
        try:
            val_max = int(sys.argv[3])
        except:
            val_max = 0
        print(random_number(val_min, val_max))
    elif (sys.argv[1] == "f"):
        print(random_file(False))
    elif (sys.argv[1] == "F"):
        print(random_file(True))
    else:
        print("Unknown command")


if __name__ == "__main__":
    sys.exit(main())
