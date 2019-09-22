import numpy as np
import csv
import os
import scipy.io as sio
import sys
from collectpara import csv2mat

path=sys.argv[1]
matname=sys.argv[2]

csv2mat(path,matname)
'''
dtlist=[30,60,300,600]
dirs=range(11,11+len(dtlist))

for i in range(len(dtlist)):
    path="/vol6/home/zhangxy_zj/YinHQ/LTRANSv.2b-master/Model6."+str(dirs[i])+"/"
    matname="3dLOC_20130916_44_eddy2_layer22_dt"+str(dtlist[i])+".mat"
    print(path,matname)
    csv2mat(path,matname)

'''
