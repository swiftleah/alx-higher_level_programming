#!/usr/bin/python3

import sys
argv = sys.argv[1:]

total = sum(int(arg) for arg in argv)
print("{}".format(total))
