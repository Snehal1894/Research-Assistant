import os

def filewrite(name):
	f1=open("temp.narrowPeak","w+")
	f2=open(name,"r")
	con=f2.readlines()
	for i in range(len(con)):
		en=con[i].split('\t')
		start=int(en[1])
		end=int(en[2])
		peak=(start+end)/2
		start=peak-75
		end=peak+75
		li=en[0]+"\t"+str(start)+"\t"+str(end)
		for j in range(3,len(en)):
			li=li+"\t"+en[j]
		#print start, end, peak
		#print li
		f1.write(li)
	
		


fs=os.popen("ls factorwise")
op=fs.readlines()
for i in op:
   	i=i.rstrip('\n')
        f1=os.popen("ls factorwise/"+i+"/sortedpeaks/")
	for j in f1.readlines():
		if "_r." in j:
			j=j.rstrip('\n')
			#os.popen("rm "+"factorwise/"+i+"/"+j+".fa")
			fn="factorwise/"+i+"/sortedpeaks/"+j
			filewrite(fn)
			os.popen("rm "+fn)
			#name=j.split('.')[0]+"_r.narrowPeak"
			os.popen("mv temp.narrowPeak "+j)
			os.popen("mv "+j+" factorwise/"+i+"/sortedpeaks/")
		
	print "done",i
		


	

	


