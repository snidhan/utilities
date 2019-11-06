#!/bin/bash

# Script for obtaining datafiles from folder

echo "Bash version ${BASH_VERSION}..."

nstart=2400000
nend=2880000

folder=/archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/plnfiles_gaffney_all

for i in {02600000..02880000..1000}
do
    echo $i
    filename="U0_090deg_j0065_n$i.pln"
    echo $filename
    archive get -C $folder $filename
done

for i in {02600000..02880000..1000}
do
    echo $i
    filename="W0_090deg_j0065_n$i.pln"
    echo $filename
    archive get -C $folder $filename
done

for i in {02600000..02880000..1000}
do
    echo $i
    filename="DENSF_090deg_j0065_n$i.pln"
    echo $filename
    archive get -C $folder $filename
done

for i in {02600000..02880000..1000}
do
    echo $i
    filename="omgt_090deg_j0065_n$i.pln"
    echo $filename
    archive get -C $folder $filename
done

for i in {02600000..02880000..1000}
do
    echo $i
    filename="omgz_090deg_j0065_n$i.pln"
    echo $filename
    archive get -C $folder $filename
done
