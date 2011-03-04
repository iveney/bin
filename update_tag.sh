#!/bin/bash

for i in *.mp3
do
	#echo $i
	new_name=`./fw2ascii.py "$i"`
	mv "$i" "$new_name"
done
