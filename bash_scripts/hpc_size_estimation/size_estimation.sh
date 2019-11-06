#!/bin/bash

#Script for estimation of the number of files

common_den=_background_gaffney

# Estimation of datafiles

filename="datafiles$common_den"
cd ./$filename
ls -l *.5p | wc -l


filename="spodfiles$common_den"
cd ./$filename
ls -l *.spod | wc -l

filename="plnfiles$common_den"
cd ./$filename
ls -l *.pln | wc -l

filename="tnofiles$common_den"
cd ./$filename
ls -l *.tno | wc -l


