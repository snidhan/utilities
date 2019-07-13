#!/bin/bash
# Script for deleting certain plnfiles

 nstart=500
 nend=1500


for filename in *.res

do 
   echo $filename
   string=$(awk -F'[_.]' '{printf $2}' <<< "${filename}")
   #echo $string
   #s=${string:1:8}
   #echo $s
   number=$((10#$string+0))
   echo $number

   if [[ "$number" -lt $nend &&  "$number" -gt $nstart ]]; then
    echo "removing $filename"
    rm $filename
   fi

done

