#!/bin/bash

DIR_DATAFILES=/archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/datafiles_background_gaffney/
DIR_SPODFILES=/archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/spodfiles_background_gaffney/
DIR_PLNFILES=/archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/plnfiles_background_gaffney/
DIR_TNOFILES=/archive/home/snidhan/spod_re5e4_fr2_koehrgaffney/tnofiles_background_gaffney/
#DIR_RUNi=

SYSTEM_NAME=snidhan@gaffney.navydsrc.hpc.mil

rsync -r --progress $SYSTEM_NAME:$DIR_DATAFILES* ./datafiles/
rsync -r --progress $SYSTEM_NAME:$DIR_SPODFILES* ./spodfiles/
rsync -r --progress $SYSTEM_NAME:$DIR_PLNFILES*  ./plnfiles/
rsync -r --progress $SYSTEM_NAME:$DIR_TNOFILES*  ./tnofiles/
