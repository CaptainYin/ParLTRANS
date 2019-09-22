import os
root='./'
list=os.listdir(root)
list.sort()
for i in range(1,9):
	print(i)
	os.system("ncks -d ocean_time,0,,12 scs10_his_000"+str(i)+".nc ../12hour/scs10_his_000"+str(i)+".nc")
	#path=os.path.join(root,list[i])
	#if os.path.isdir(path):
	#	os.system("mv "+path+"/scs10_his_0001.nc ./scs10_his_00"+str(i+1).zfill(2)+".nc")
	#	os.system("mv "+path+"/scs10_his_0002.nc ../halfhour/scs10_his_00"+str(i*4+2).zfill(2)+".nc")
	#	os.system("mv "+path+"/scs10_his_0003.nc ../halfhour/scs10_his_00"+str(i*4+3).zfill(2)+".nc")
	#	os.system("mv "+path+"/scs10_his_0004.nc ../halfhour/scs10_his_00"+str(i*4+4).zfill(2)+".nc")
		#print path,i
		#os.system("cp "+path+"/ocean_scs10_cur_daily.in "+path+"/ocean_scs10_cur.in")
		#os.system("ls "+path)

	'''	with open(path+"/ocean_scs10_cur.in",'r') as f:
		      lines=f.readlines()
		      with open(path+"/ocean_scs10_cur.in",'w') as f_w:
			    for line in lines:
			         if "NHIS == 240" in line:
                                         line="  NHIS == 5\n"
				 if "NDEFHIS == 960" in line:
					 line="  NDEFHIS == 240\n"
		                 f_w.write(line.encode('utf-8'))
       ''' 
