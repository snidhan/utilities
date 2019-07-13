#!/bin/bash
echo "--------------------"
echo $$
echo $$ >pid_file
echo  "($HOSTNAME)" >node_login
for i in $(seq 1 28800000)
do
sleep 1m
rm qview_grep.dat
qstat | grep 'new_trip1' > qview_grep.dat  # Change
if grep -q new_trip1 qview_grep.dat; then  # Change
    echo found: do nothing
    cat qview_grep.dat | grep 'new_trip1'  # Change
    echo $$ >pid_file
else
    echo not found: submit new job
    qsub sturb.job.onyx    
    echo  "($HOSTNAME)" >node_login
    echo $$ >pid_file
fi
done


