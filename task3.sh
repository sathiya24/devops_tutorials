#!/bin/bash

src1=$1
dst1=$2
flag=$3

echo $flag

if [ $flag = "1" ]
  then  
      x=`diff $1 $2`
      if [ "$x" != "" ]
  then 
      echo "there is difference"
else
      echo "no difference" 
fi
else
    x=`diff $1 $2`
    if [ "$x" != "" ]
then 
     echo "already exists"
     rsync -avu "$1/" "$2"
     rsync -avu "$2/" "$1"
    echo "copied"
else
    echo "no difference"
fi
fi
