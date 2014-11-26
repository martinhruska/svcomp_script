#! /usr/bin/python

import subprocess
import sys
sys.path.append('../fa_build')
import sv_comp_run
import os

for i in ['f0001', 'f0002', 'f0003', 'f0004', 'f0005', 'f0006', 'f0007', 'f0009', 'f0010', 'f0011', 'f0012', 'f0013', 'f0014', 'f0016', 'f0019',\
        'f0020', 'f0022', 'f0024', 'f0025', 'f0027', 'f0028', 'f0029', 'f0030', 'f0036', 'f0037', 'f0039', 'f0040', 'f0042', 'f0044', 'f0045',\
        'f0047', 'f0048', 'f0052', 'f0055', 'f0100', 'f0101', 'f0102', 'f0103', 'f0105', 'f0106', 'f0110', 'f0111', 'f0114', 'f0117', 'f0118',\
        'p0001', 'p0003', 'p0023', 'p0027', 'p0028', 'p0029', 'p0037', 'p0042', 'p0045', 'p0046', 'p0075', 'p0076', 'p0085', 'p0091', 'p0119',\
        'p0126', 'p0143', 'p0170','p0175']:
    args = sv_comp_run.parseParams(sys.argv[1:])
    args[sv_comp_run.FILE_PARAM] = os.path.join('../tests', 'forester-regre', 'test-'+i+'.c')
    res = sv_comp_run.execute(args)
    err = os.path.join('../tests', 'forester-regre', 'test-'+i+'.err')
    with open(err,'r') as f:
        numbs = ''
        for l in f.readlines():
            if not "writing memory" in l and not "warning:" in l:
                numbs += l
        num = len(numbs)
        if num == 0 and res == 0:
            print "OK"
        elif num > 0 and res == 1:
            print "OK"
        else:
            print "FAIL",err,numbs,num,res
