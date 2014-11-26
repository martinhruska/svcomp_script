#! /bin/bash

FAPATH=/home/martin/temp/forester-svcomp

for k in `cat /home/martin/forester/fa/sv-comp/c/$1.set`
do
	for i in `ls /home/martin/forester/fa/sv-comp/c/$k`;
	do
		echo $i >> $3
		timeout 100 $FAPATH/fa_build/sv_comp_run.py --trace $FAPATH/fa/sv-comp/witness/`basename $i`".xml" --time $i >> $3
	done
done
