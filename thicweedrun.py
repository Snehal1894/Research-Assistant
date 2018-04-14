import os

#f1=os.popen("ls chipseq_encode/reqfasta")
#s1=f1.readlines()
#print s1
s1=["USF1","USF2","YY1","ZBED1","ZBTB33","ZBTB7A"]
for tf in s1:
	cmd1="ls chipseq_encode/reqfasta/"+tf
	f2=os.popen(cmd1)
	s2=f2.readlines()
	#print s2
	for fl in s2:
		fl=fl.strip('\n')
		cmd2="julia chipseq_encode/thicweed.jl chipseq_encode/reqfasta/"+tf+"/"+fl+" > log.txt"
		print cmd2		
		os.popen(cmd2)
		print 'done'
