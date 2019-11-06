#!/bin/bash

# Script for obtaining datafiles from folder

echo "Bash version ${BASH_VERSION}..."

nstart=2329600
nend=2887400

folder=/erdc1/snidhan/fr2_files/datafiles/

for i in {02887500..03057500..2500}
do
    echo $i

    filename="u_$i.res"
#    echo $filename
#    archive get -C $folder $filename
	rsync -r --progress $filename /archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/resfiles_background_gaffney/

    filename="v_$i.res"
#    echo $filename
#    archive get -C $folder $filename
	rsync -r --progress $filename /archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/resfiles_background_gaffney/

    filename="w_$i.res"
#    echo $filename
#   archive get -C $folder $filename
	rsync -r --progress $filename /archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/resfiles_background_gaffney/

    filename="dens_$i.res"
#    echo $filename
#   archive get -C $folder $filename
	rsync -r --progress $filename /archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/resfiles_background_gaffney/

    filename="p_$i.res"
#    echo $filename
#   archive get -C $folder $filename
	rsync -r --progress $filename /archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/resfiles_background_gaffney/

    filename="tv_$i.res"
#    echo $filename
#   archive get -C $folder $filename
	rsync -r --progress $filename /archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/resfiles_background_gaffney/
done
