#! /bin/bash

GCC=/usr/bin/gcc-4.6
FAPATH=/home/martin/temp/forester-svcomp

for k in `cat /home/martin/forester/fa/sv-comp/c/$1.set`
do
	for i in `ls /home/martin/forester/fa/sv-comp/c/$k`;
	do
		echo $i >> $2
		timeout 60 $GCC -I $FAPATH/include/forester-builtins -o /dev/null -O0 -DFORESTER -fplugin=$FAPATH/fa_build/libfa.so "-fplugin-arg-libfa-args=print-trace-svcomp;trace-file:temp.txt" $i 2>> $2
		echo "" >> $2
		echo "" >> $2
	done
done

rm temp.txt
