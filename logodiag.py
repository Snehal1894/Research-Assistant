import os

s1=["USF1","USF2","YY1","ZBED1","ZBTB33","ZBTB7A","ZEB1","ZKSCAN1","ZNF143","ZNF263","ZNF274","ZNF384"]
for tf in s1:
	print tf.rstrip('\n')
	os.popen("mkdir apache-tomcat-8.5.12/webapps/Logoresults/Logos/"+tf.rstrip('\n'))
	cmd1="ls chipseq_encode/reqfasta/"+tf
	f2=os.popen(cmd1)
	s2=f2.readlines()
	for fl in s2:
		if "fa_archs.txt" in fl :
			fl=fl.rstrip('\n')
			cmd2="python archs2svg.py chipseq_encode/reqfasta/"+tf+"/"+fl+" > apache-tomcat-8.5.12/webapps/Logoresults/Logos/"+tf+"/"+fl.split('fa')[0]+"svg"
			print cmd2
			os.popen(cmd2)
