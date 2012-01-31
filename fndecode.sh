#!/bin/bash
# decode the filenames that are url encoded 

cd "$1"
for i in `ls %*`;do
	name=`urldecode "$i"`
	echo "changing '$i' to '$name'"
	mv "$i" "$name"
done
