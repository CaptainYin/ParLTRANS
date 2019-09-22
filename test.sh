#!/bin/sh
for i in {1,2};
do
#   mkdir 'ede'+$i
	cd /vol/home/student/YinHQ/roms/LTRANSv.2b-master/Model3.$i/
	./LTRANS.exe >& run.log
	echo $i
done
