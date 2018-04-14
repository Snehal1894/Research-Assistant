import os

fs=os.popen("ls factorwise")
op=fs.readlines()
f2=open("mergesort.sh",'w')
for i in op:
   	i=i.rstrip('\n')
        f1=os.popen("ls factorwise/"+i+"/sortedpeaks/")
	for j in f1.readlines():
		if "_r." in j:
			j=j.rstrip('\n')
			f2.write("sort -k1,1 -k2,2n factorwise/"+i+"/sortedpeaks/"+j+" -o factorwise/"+i+"/sortedpeaks/"+j+" | head -0"+"\n")
			f2.write("bedtools merge -i factorwise/"+i+"/sortedpeaks/"+j+" | head -0"+"\n")
	f2.write("echo "+i+"\n")
f2.close()

