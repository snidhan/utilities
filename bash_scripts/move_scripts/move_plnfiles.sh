#!/bin/bash

# Script for obtaining datafiles from folder

echo "Bash version ${BASH_VERSION}..."

nstart=2329600
nend=2887400

folder=/erdc1/snidhan/fr2_files/datafiles/

for i in {02776600..02820000..100}
do
    echo $i
    cp -r ../plnfiles_gaffney_all/*$i* ./
done
