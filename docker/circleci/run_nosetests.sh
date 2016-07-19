#!/bin/bash
for i in /etc/profile.d/*.sh; do
    source $i
done
source activate nipypetests-2.7
cd /root/src/nipype
mkdir -p /scratch/nose
nosetests --with-doctest -c /root/src/nipype/.noserc --logging-level=DEBUG --verbosity=3 $@
