#!/bin/bash

for filename in ./*.pln; do
    fname=$(echo $filename | cut -c 3-)
    var=$(echo $fname | cut -d'_' -f 1)
    ang=$(echo $fname | cut -d'_' -f 2)
    jidx=$(echo $fname | cut -d'_' -f 3)
    fname=$(echo ${var}_${ang}_${jidx})
    echo $fname
    n=$(echo $filename| cut -d'_' -f 4)
    n=${n%.pln}
    n=${n#"n"}
    n=$(echo $n | sed 's/^0*//')
    echo $n
    sed -i '7s/.*/ '$n'/' run_pln
    sh run_pln $fname
done
