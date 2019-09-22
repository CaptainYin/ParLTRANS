#!/bin/sh
dts=[1,5,30,60]
for ((i=1;i<=4;i++));
do
    echo $(dts[i]+3)
#	cp /vol/home/student/YinHQ/roms/LTRANSv.2b-master/Model4.$i/output/3d*  loc/
 #    rm Model6.$i.* -r
#    rm  Model6.$i/input/*
done

#python collectpara1.py Model6.3/ 3dLOC_20130916_261_eddy2_layer35_dt1.mat
#python collectpara1.py Model6.4/ 3dLOC_20130916_261_eddy2_layer35_dt3.mat
#python collectpara1.py Model6.5/ 3dLOC_20130916_261_eddy2_layer35_dt5.mat
#python collectpara1.py Model6.6/ 3dLOC_20130916_261_eddy2_layer35_dt30.mat
#python collectpara1.py Model6.7/ 3dLOC_20130916_261_eddy2_layer35_dt50.mat
#python collectpara1.py Model6.8/ 3dLOC_20130916_261_eddy2_layer35_dt300.mat
#python collectpara1.py Model6.9/ 3dLOC_20130916_261_eddy2_layer35_dt600.mat
#python collectpara1.py Model6.10/ 3dLOC_20130916_261_eddy2_layer35_dt3600.mat
#python collectpara1.py Model6.11/ 2dLOC_20130916_261_eddy2_layer35_dt1.mat
#python collectpara1.py Model6.12/ 2dLOC_20130916_261_eddy2_layer35_dt3.mat
#python collectpara1.py Model6.13/ 2dLOC_20130916_261_eddy2_layer35_dt5.mat
#python collectpara1.py Model6.14/ 2dLOC_20130916_261_eddy2_layer35_dt30.mat
#python collectpara1.py Model6.15/ 2dLOC_20130916_261_eddy2_layer35_dt50.mat
#python collectpara1.py Model6.16/ 2dLOC_20130916_261_eddy2_layer35_dt300.mat
#python collectpara1.py Model6.17/ 2dLOC_20130916_261_eddy2_layer35_dt600.mat
#python collectpara1.py Model6.18/ 2dLOC_20130916_261_eddy2_layer35_dt3600.mat
