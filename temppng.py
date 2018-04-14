import os

c1=os.popen("ls Logos")
s1=c1.readlines()

#f1=open("Pngconvert.sh","w")

for tf in s1:
	tf=tf.rstrip('\n')
	#os.popen("rm -r "+tf)
	os.popen("mkdir Logospng/"+tf)
	c2=os.popen("ls Logos/"+tf)
	s2=c2.readlines()
	for img in s2:
		os.popen("./svg2png.sh Logos/"+tf+"/"+img.rstrip('\n')+"\n")
		os.popen("mv "+img.split(".svg")[0]+".png Logospng/"+tf)
        print "done"+tf

#f1.close()
		
