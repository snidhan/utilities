#!/bin/bash

# Script for obtaining datafiles from folder

echo "Bash version ${BASH_VERSION}..."

nstart=2329600
nend=2887400

folder=/erdc1/snidhan/fr2_files/datafiles/

for i in {02329600..02887400..100}
do
    echo $i
    filename="up_$i.res"
    echo $filename
#    archive get -C $folder $filename
done
