import os

fs=os.popen("ls factorwise")
op=fs.readlines()
for i in op:
	i=i.rstrip('\n')
	f1=os.popen("ls factorwise/"+i+"/sortedpeaks/")
	for j in f1.readlines():
		j=j.rstrip('\n')
		if "_r.narrowPeak" in j:
			name=j.split("_r")[0]
			os.popen("bedtools getfasta -fi hg19.genome.fa -bed factorwise/"+i+"/sortedpeaks/"+j+" -fo "+name+".fa")
			os.popen("mv "+name+".fa "+" factorwise/"+i)
	print "done", i


