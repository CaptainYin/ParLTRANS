import numpy as np
import csv
import os
import scipy.io as sio
import sys
import time
from replace import ExistString

def csv2mat(path,matname):
#	print(!ExistString(path+'run.log','END LTRANS'))
#	while ExistString(path+'run.log','END LTRANS')==False:
#	     time.sleep(30)
			 #print('sleep 3 sec')
    path=path+'output/'
    filelist=os.listdir(path)
    filelist.sort()
#	filelist=filelist[0:1126]
    loc=np.loadtxt(open(path+filelist[1],'rb'),delimiter=',',usecols=(0,2,3))
    if(len(loc.shape)!=1):
        LOC=np.zeros((loc.shape[0],loc.shape[1],len(filelist)-1))
        for i in range(1,len(filelist)):
		    loc=np.loadtxt(open(path+filelist[i],'rb'),delimiter=',',usecols=(0,2,3))
		    LOC[:,0,i-1]=loc[:,0]
		    LOC[:,1,i-1]=loc[:,1]
		    LOC[:,2,i-1]=loc[:,2]
    else:
        LOC=np.zeros((1,3,len(filelist)-1))
        for i in range(1,len(filelist)):
		    loc=np.loadtxt(open(path+filelist[i],'rb'),delimiter=',',usecols=(0,2,3))
		    LOC[:,0,i-1]=loc[0]
		    LOC[:,1,i-1]=loc[1]
		    LOC[:,2,i-1]=loc[2]
    sio.savemat('../loc/wbc20/'+matname,{'LOC':LOC})
if __name__ == '_mian_':
	path=sys.argv[1]
	matname=sys.argv[2]
	csv2mat(path,matname)
