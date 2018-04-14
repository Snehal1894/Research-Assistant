from __future__ import division
import operator
import os

dict1 ={}

f1=os.popen("ls factorwise")
s1=f1.readlines()

for tf in s1:
	tf=tf.rstrip('\n')
	f2=os.popen("ls factorwise/"+tf)
	s2=f2.readlines()
	for fl in s2:
		fl=fl.rstrip('\n')
		if os.path.isfile("factorwise/"+tf+"/"+fl):
			#print tf+"/"+fl+" ",
			#print len(open("factorwise/"+tf+"/"+fl,"r").readlines())/2
			dict1["factorwise/"+tf+"/"+fl]=len(open("factorwise/"+tf+"/"+fl,"r").readlines())/2

sdict = sorted(dict1.items(), key=operator.itemgetter(1))
print type(sdict)
fw=open("encodefilesrun.txt","w")
for k,v in sdict:
	#print k+":"+str(v)
	fw.write(k+"\n")

fw.close()
