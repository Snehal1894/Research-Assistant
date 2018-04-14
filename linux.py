import os
import fimo2arch
f=os.popen("ls 1000seq")
s= f.readlines()
#print s

for fname in s:
	#arch=fname.split("/")[2].split(".")[0]+"."+fname.split("/")[2].split(".")[1]
	#arch=fname.split(".")[0]+"."+fname.split(".")[1]
	arch=fname.split(".fa")[0]
	print arch
	os.popen("meme-chip -dreme-m 0 1000seq/"+fname.rstrip('\n'))
	print "meme-chip done"
	fs=os.popen("find ./memechip_out/ -type f -name fimo.txt")
	op=fs.readlines()
	fimo2arch.main(arch,op)
	os.popen("mv memechip_out memechip_out_"+arch)
	os.popen("mv memechip_out_"+arch+" memeop")
	os.popen("mv "+arch+".txt arch1000")
	print "done ",arch



