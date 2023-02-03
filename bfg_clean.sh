#!/bin/bash
for dir in $(ls -d */); do
	java -jar bfg.jar --replace-text secrets.txt $dir.git
	echo "Replaced keys in $dir"
done 