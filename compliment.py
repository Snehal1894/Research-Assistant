import os

c1=os.popen("ls Logospng")
s1=c1.readlines()
for tf in s1:
	tf=tf.rstrip('\n')
	print tf
	os.popen("mkdir Logos_do/"+tf)
	c2=os.popen("ls Logospng/"+tf)
	s2=c2.readlines()
	c3=os.popen("ls Logospng_old/"+tf)
	s3=c3.readlines()
	for fl in s2:
		if fl not in s3:
			fl= fl.rstrip('\n')
			print fl
			os.popen("mv Logospng/"+tf+"/"+fl+" Logos_do/"+tf)
	

	
