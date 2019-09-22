#!/bin/sh
#source ~/.bashrc
for ((i=49;i<=70;i++));
do
	cd /vol6/home/zhangxy_zj/YinHQ/LTRANSv.2b-master/Model4.$i/
	seq= `grep "\<parnum>\" LTRANS.data | awk '{print $2}'`
        echo $seq
#	echo running Model4.$i
done
