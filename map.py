import os
import csv
import numpy as np
import replace
#split iniloc file
parf='IPL_20130913_4590_eddy2'
parent_dir='Model6.5'
jobscript_prefix='6_5'
MapNum=96
parfpath='../loc/wbc20/'+parf+'.csv'
loc=np.loadtxt(open(parfpath,'rb'),delimiter=',',usecols=(0,1,2,3))
offset=loc.shape[0]/MapNum
res=loc.shape[0]%MapNum
num=np.zeros((MapNum,),dtype=np.int)
for i in range(0,MapNum):
    parf0=parf+'_'+str(i)
    parfpath0='../loc/wbc20/'+parf0+'.csv'
    if(i<res):
        np.savetxt(parfpath0,loc[i*(offset+1):(i+1)*(offset+1),:],fmt='%f',delimiter=',')
        num[i]=loc[i*(offset+1):(i+1)*(offset+1),:].shape[0]
    else:
        np.savetxt(parfpath0,loc[i*offset+res:(i+1)*offset+res,:],fmt='%f',delimiter=',')
        num[i]=loc[i*offset+res:(i+1)*offset+res,:].shape[0]
'''
	if(i==MapNum-1):
		np.savetxt(parfpath0,loc[i*offset:,:],fmt='%f',delimiter=',')
		num[i]=loc[i*offset:,:].shape[0]
	#	print(loc[i*offset:-1,:].shape[0],'sdfg')
	else:
		np.savetxt(parfpath0,loc[i*offset:(i+1)*offset,:],fmt='%f',delimiter=',')
		num[i]=loc[i*offset:(i+1)*offset,:].shape[0]
		#print(loc[i*offset:(i+1)*offset,:].shape[0])
'''
print(num,num.sum())


#create working directory
os.system("rm "+parent_dir+"/output/*")
for i in range(0,MapNum):
	os.system("rm "+parent_dir+"."+str(i)+" -r")
for i in range(0,MapNum):
	os.system("cp "+parent_dir+" "+parent_dir+"."+str(i)+" -r")
	os.system("mv "+parent_dir+"."+str(i)+"/"+jobscript_prefix+" "+parent_dir+"."+str(i)+"/"+jobscript_prefix+"."+str(i))
	parameterfile=parent_dir+"."+str(i)+"/LTRANS.data"
	name="parfile"
	value='\'../../loc/wbc20/'+parf+'_'+str(i)+'.csv\''
	replace.setparameter(parameterfile,name,value)
	replace.setparameter(parameterfile,"Numpar",str(num[i]))

#run
#for i in range(0,MapNum):
	#os.system("cd /vol6/home/zhangxy_zj/YinHQ/LTRANSv.2b-master/"+parent_dir+"."+str(i))
	#os.system("pwd")
#	os.system("yhbatch -N 1 -n 1 -p weather "+jobscript_prefix+"."+str(i))

'''
#list=os.listdir(root)
#list.sort()

#for i in range(1,9):
#	print(i)
#	os.system("ncks -d ocean_time,0,,12 scs10_his_000"+str(i)+".nc ../12hour/scs10_his_000"+str(i)+".nc")
	#path=os.path.join(root,list[i])
	#if os.path.isdir(path):
	#	os.system("mv "+path+"/scs10_his_0001.nc ./scs10_his_00"+str(i+1).zfill(2)+".nc")
	#	os.system("mv "+path+"/scs10_his_0002.nc ../halfhour/scs10_his_00"+str(i*4+2).zfill(2)+".nc")
	#	os.system("mv "+path+"/scs10_his_0003.nc ../halfhour/scs10_his_00"+str(i*4+3).zfill(2)+".nc")
	#	os.system("mv "+path+"/scs10_his_0004.nc ../halfhour/scs10_his_00"+str(i*4+4).zfill(2)+".nc")
		#print path,i
		#os.system("cp "+path+"/ocean_scs10_cur_daily.in "+path+"/ocean_scs10_cur.in")
		#os.system("ls "+path)

		with open(path+"/ocean_scs10_cur.in",'r') as f:
		      lines=f.readlines()
		      with open(path+"/ocean_scs10_cur.in",'w') as f_w:
			    for line in lines:
			         if "NHIS == 240" in line:
                                         line="  NHIS == 5\n"
				 if "NDEFHIS == 960" in line:
					 line="  NDEFHIS == 240\n"
		                 f_w.write(line.encode('utf-8'))
       '''
