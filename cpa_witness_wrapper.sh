#! /bin/bash

# param 1 - path to scripts/cpa.sh
# param 2 - witness
# param 3 - property
# param 4 - test case

ACT_PATH=`pwd`
RES=`cd $1 && $1/scripts/cpa.sh -witness-check -spec "$ACT_PATH/$2" -spec $3 $4 2>/dev/null`

if [ -n "`echo $RES | grep FALSE`" ]; then
	echo `basename "$4"` "[OK]"
	exit 0
else
	echo `basename $4` "[FAIL]"
	exit 1
fi
