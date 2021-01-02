#!/bin/bash
## Script for copying restart files from archive

echo "Bash Version ${BASH_VERSION}..."

i=0
one=1
nstart=300000
nend=310000
stride=1000
path="/erdc1/karu/Disk_15e4_1/RESTART_FILES/"
var="u_"
while [ $i -le 10 ]
do 
	#filenum=$nstart
	#echo $filenum
	filenum=$(( $nstart+ $(( $i-1)) * $stride ))
	echo $filenum
	i=$(( $i+1 ))
	echo $i
	padfilenum=$(printf "%08d\n" $filenum)
	echo $padfilenum
	res=".res"
	fullfile="$var$padfilenum$res"
	echo $fullfile
	archive get -C $path -S $fullfile
done
 
 
 
var="v_"
while [ $i -le 10 ]
do 
	#filenum=$nstart
	#echo $filenum
	filenum=$(( $nstart+ $(( $i-1)) * $stride ))
	echo $filenum
	i=$(( $i+1 ))
	echo $i
	padfilenum=$(printf "%08d\n" $filenum)
	echo $padfilenum

	res=".res"
	fullfile="$var$padfilenum$res"
	echo $fullfile	
	archive get -C $path -S $fullfile
done
 
var="w_"
while [ $i -le 10 ]
do 
	#filenum=$nstart
	#echo $filenum
	filenum=$(( $nstart+ $(( $i-1)) * $stride ))
	echo $filenum
	i=$(( $i+1 ))
	echo $i
	padfilenum=$(printf "%08d\n" $filenum)
	echo $padfilenum

	res=".res"
	fullfile="$var$padfilenum$res"
	echo $fullfile	
	archive get -C $path -S $fullfile
done
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
