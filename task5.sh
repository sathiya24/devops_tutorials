echo "#!/bin/bash

src1=$1
dst1=$2

SAME=0
x=`diff $1 $2`
if [ "$x" != "" ]
then 
echo "already exists"

if [ "$x" == "" ]
SAME=1
rsync -avu "$1/" "$2"
rsync -avu "$2/" "$1"
echo "copied"
else
echo "no difference"
echo "$SAME"
fils




"
