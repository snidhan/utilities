#! /bin/bash
# Script for deleting certain restart files, tnofile, plnfiles

  n=100000


for i in *.pln
do
  #echo "${i#*_}"
  #echo "${i:2:8}" 
  
  #this is called shell parameter expansion 
  # extract number from w_number.res
  
  str="${i:2:8}" 
  number=$((10#$str+0))
 
  #echo $str 
  #echo $number 

 if [ "$number" -lt $n ]; then

 echo "removing $i"
 rm $i
 

 fi 

done 

        
