#! /bin/bash

for dir in *
do
	if [ -d $dir ]; then 
		dot=true
		cd $dir;
	else 
		dot=false
	fi
	echo $(pwd)
	rename -n 's/\-\-/\-/g' *.mp4;
	if $dot; then
		cd ..;
	fi
done
