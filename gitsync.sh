#!/bin/bash
#
#
if [ "$#" -ne 2 ]; then
	echo "Illegal number of parameters"
	echo "Usage: $0 arg1 arg2"
	exit 2
fi
FILETOADD=$1
COMMENT=$2
git add $1
git commit -m $2
git push
