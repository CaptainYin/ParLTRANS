import numpy as np
import time
import csv
import os
import sys
import scipy.io as sio
from collectpara import csv2mat
from multiprocessing import Pool,cpu_count
#for example :Modelnum is 6.7 ,matname is 6_7
'''
def reduce(Arg):
    Modelnum=Arg[0],matname=Arg[1]
	Mapnum=48
	for i in range(0,Mapnum):
		csv2mat('Model'+Modelnum+'.'+str(i)+'/',matname+'_'+str(i)+'.mat')

	for i in range(0,Mapnum):
		data=sio.loadmat('../loc/wbc20/'+matname+'_'+str(i)+'.mat')
		if(i==0):
			LOC=data['LOC']
		else:
			LOC=np.concatenate((LOC,data['LOC']),axis=0)
	sio.savemat('../loc/wbc20/'+matname+'.mat',{'LOC':LOC})
'''
def csv2mat4par(Arg):
    csv2mat(Arg[0],Arg[1])
def reduce(Modelnum,matname):
    Mapnum=96
    pool=Pool(cpu_count())
    pool.map(csv2mat4par,[('Model'+Modelnum+'.'+str(i)+'/',matname+'_'+str(i)+'.mat') for i in range(0,Mapnum)])
    for i in range(0,Mapnum):
		data=sio.loadmat('../loc/wbc20/'+matname+'_'+str(i)+'.mat')
		if(i==0):
			LOC=data['LOC']
		else:
			LOC=np.concatenate((LOC,data['LOC']),axis=0)
    sio.savemat('../loc/wbc20/'+matname+'.mat',{'LOC':LOC})

Modelnum=sys.argv[1]
matname=sys.argv[2]
reduce(Modelnum,matname)
