#! /usr/bin/python

import sys

RES_TRUE = "TRUE"
RES_UNKNOWN = "UNKNOWN"
RES_FALSE = "FALSE"

NAME_TRUE = "true"
NAME_FALSE = "false"

RESL = [RES_TRUE, RES_FALSE]
RESN = [NAME_TRUE, NAME_FALSE]
FALSEL = ["valid-memtrack", "valid-deref", "valid-free"]
FALSEU = "unreach"

def evalRes(name, res):
    if RES_UNKNOWN in res:
        return 0
    elif RES_TRUE in res:
        if NAME_TRUE in name:
            return 2
        else:
            print "FALSE NEGATIVE", name, res
            return -12
    elif RES_FALSE in res:
        for i in FALSEL:
            if i in res and i not in name:
                print "FALSE POSITIVE", name, res
                return -6
            elif i in res and i in name:
                return 1
        if NAME_TRUE in name:
            print "FALSE POSITIVE", name, res
            return -6
        elif FALSEU in name:
            return 1
    return None

       
def evalTest(test):
    if NAME_TRUE in test:
        return 2
    elif NAME_FALSE in test:
        return 1
    else:
        print test

### main
f = open(sys.argv[1])
i = 0
name = ""
points = 0
allpoints = 0

for l in f:
    l = l.strip()
    if i == 0:
        name = l
        allpoints += evalTest(name)
    elif i == 1:
        if RES_TRUE not in l and RES_FALSE not in l and RES_UNKNOWN not in l:
            name = l
            i = 1
            continue
        points += evalRes(name, l)
    i = (i+1)%3

print "Dead Palestinian:",points, "Dead Jews:",allpoints
