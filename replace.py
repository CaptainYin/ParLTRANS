def setparameter(file,name,value):
	with open(file,'r') as f:
		lines=f.readlines()
        with open(file,'w') as f_w:
                for line in lines:
            	      if name in line:
                           line=name+" = " +value+"\n"
            	      f_w.write(line.encode('utf-8'))

def ExistString(file,string):
	#print(file,string)
	with open(file,'r') as f:
		lines=f.readlines()
	for line in lines:
		if string in line:
			return True
	return False

#print(ExistString('Model6.3.0/run.log','END LTRANS'))

#filelist=['IPL_layer6_1000uni_r30.csv','IPL_layer7_1000uni_r30.csv','IPL_layer8_1000uni_r30.csv','IPL_layer9_1000uni_r30.csv','IPL_layer10_1000uni_r30.csv','IPL_layer11_1000uni_r30.csv','IPL_layer12_1000uni_r30.csv','IPL_layer15_1000uni_r30.csv']
'''
#dtlist=['5','30','60','300','600']
dirs=range(24,48)
for i in range(len(dirs)):
    file="/vol6/home/zhangxy_zj/YinHQ/LTRANSv.2b-master/Model6.6."+str(dirs[i])+"/LTRANS.data"
    name="idt"
    value='600'
    print(file,value)
    setparameter(file,name,value)
'''
