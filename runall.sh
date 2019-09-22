#!/bin/sh


for ((i=24;i<48;i++));
do
 #cp Model4/LTRANS.data Model4.$i/ -r
#cp Model4  Model4.$i -r
#mv Model4.$i/4  Model4.$i/4_$i
#	rm Model4.$i/output/* -r
#	rm Model3.$i/*out
#	rm Model3.$i/run.log
#	rm Model4.$i/run.log

	cd /vol6/home/zhangxy_zj/YinHQ/LTRANSv.2b-master/Model6.6.$i/
	yhbatch -N 1 -n 1 -p weather  6_6.$i

#	echo running $i !!!!!!!!!!!!!!!!!!!!!!
#	ls output|wc
        #tail -3 run.log
#        python collectpara.py Model4.$i/output/  4_$i.mat
#        mv Model4.$i/output/4_$i.mat  loc/dttest

done

#for ((i=0;i<12;i++));
#do
#	cd /vol6/home/zhangxy_zj/YinHQ/LTRANSv.2b-master/Model6.10.$i/
#	yhbatch -N 1 -n 1 -p weather  6_10.$i
#done

