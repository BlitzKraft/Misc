#! /bin/bash
# An implementation of unix rename where it's not available. For example, a
# mac.

for dir in *
do
	if [ -d $dir ]; then 
		dot=true
		cd $dir;
		for file in *
		do
			echo $file
			echo $file.mov
			# mv $file $file.mov
		done
	else 
		dot=false
	fi
	echo $(pwd)
	if $dot; then
		cd ..;
	fi
done
