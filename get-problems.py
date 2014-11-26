#! /usr/bin/python

import sys
from collections import defaultdict

hist = defaultdict(int)
cases = defaultdict(list)
state = 0
statename = 0
actname = ""

SEG = "Segmentation fault"

with open(sys.argv[1]) as f:
    for l in f:
        l = l.strip()
        if statename == 0 and len(l) == 0:
            statename = 1
        elif statename == 1 and len(l) == 0:
            statename = 2
        elif statename == 2:
            statename = 0
            actname = l
            print actname

        if "Assertion" in l:
            hist[l] += 1
            cases[l].append(actname)
        elif state == 0:
            if "INTERNAL ERROR" in l:
                state += 1
            if SEG in l:
                hist[SEG] += 1
                cases[SEG].append(actname)
        elif state == 1:
            state += 1
        elif state == 2:
            state = 0
            hist[l] += 1
            cases[l].append(actname)



print "\n"
print "CASES"
for i in cases:
    print i,"-", cases[i]
    print ""

print "\n"
print "HISTOGRAM"

sumall = 0
for i in hist:
    print i,"-", hist[i]
    sumall += hist[i]

print "SumAll", sumall
