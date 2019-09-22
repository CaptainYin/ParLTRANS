#!/bin/sh

#cd /vol6/home/zhangxy_zj/YinHQ/LTRANSv.2b-master
for ((i=3;i<=18;i++));
do
# cp Model6.11/LTRANS.data Model6.$i/
#cp Model6.3  Model6.$i -r
#mv Model6.$i/6_3  Model6.$i/6_$i
#	rm Model4.$i/output/* -r
	#rm Model3.$i/run.log
	#rm Model3.$i/*out

#	rm Model3.$i/*out
	cd /vol6/home/zhangxy_zj/YinHQ/LTRANSv.2b-master/Model6.$i/
#        cd /vol6/home/zhangxy_zj/YinHQ/LTRANSv.2b-master/Model3.$i/
#	echo running Model4.$i !!!!!!!!!!!!!!!!!!!!!!
#	ls Model4.$i/output/|wc
        #tail -3 run.log
#        python collectpara.py Model4.$i/output/  4_$i.mat
 #       mv Model4.$i/output/4_$i.mat  loc/
       yhbatch -N 1 -n 1 -p weather 6_$i
done
