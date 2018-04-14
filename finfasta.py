import os


def filedit(name):
	global cnt
	fr=open(name,"r")
	fw=open("temp.fa","w+")
	ops=fr.readlines()
	ck=("a","g","c","t","N","n")
	i=0
	while i<len(ops):
		if all(s not in ops[i+1] for s in ck):
			fw.write(ops[i])
			fw.write(ops[i+1])
			cnt+=1
			
		i+=2
	#print i
	fw.close()
 
		


f1=os.popen("ls factorwise")
op1=f1.readlines()
for i in op1:
	i=i.rstrip('\n')
	f2=os.popen("ls factorwise/"+i) 
	os.popen("mkdir reqfasta/"+i)
	op2=f2.readlines()
	for j in op2:
		j=j.rstrip('\n')
		if ".fa" in j:
			fn="factorwise/"+i+"/"+j
			cnt=0
			filedit(fn)
			os.popen("rm "+fn)
			os.popen("mv temp.fa "+j)
			if cnt<20000:
				print cnt, j
				os.popen("mv "+j+" reqfasta/"+i)
			else:
				os.popen("mv "+j+" factorwise/"+i)
	print "done", i

