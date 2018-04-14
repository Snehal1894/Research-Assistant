import os

f=os.popen("ls 1000seq")
s=f.readlines()

for fname in s:
	fname=fname.rstrip('\n')
	mo=fname.split(".fa")[0]
	print mo
	os.popen("meme-chip 1000seq/"+fname)
	print "done"
	os.popen("mv memechip_out memechip_out_"+mo)
	os.popen("mv memechip_out_"+mo+" memeop")
	
