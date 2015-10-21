#! /bin/bash

# param 1 -- sv-comp forester script
# param 2 -- list of problems
# param 3 -- heap propers
# param 4 -- path to cpa.sh

TEMP="temp.graphml"

OK=0
FAIL=0
ALL=0

for i in `cat $2`
do
	$1 --false --trace $TEMP $i > /dev/null
	./cpa_witness_wrapper.sh $4 $TEMP $3 $i
	RES=`echo $?`
	if [ $RES == 0 ]; then
		((OK=$OK+1))
	else
		((FAIL=$FAIL+1))
	fi
	((ALL=$ALL+1))
done

echo "OK [$OK/$ALL]"
echo "FAIL [$FAIL/$ALL]"

rm $TEMP
