#! /usr/bin/python

import sys

f = open(sys.argv[1])
name = ""

for l in f:
    if l == "FALSE\n":
        print name
    name = l

f.close()
