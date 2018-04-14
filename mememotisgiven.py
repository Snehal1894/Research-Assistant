import os
import fimo2arch

f1=open("runmemechip.txt","r")
s1=f1.readlines()
for l in s1:
	arch=l.rstrip('\n').split("/")[1]
	os.popen(l.rstrip('\n'))
	print "meme-chip done"
        fs=os.popen("find ./memechip_out/ -type f -name fimo.txt")
        op=fs.readlines()
        fimo2arch.main(arch,op)
        os.popen("mv memechip_out memechip_out_"+arch)
        os.popen("mv memechip_out_"+arch+" memeop")
        os.popen("mv "+arch+".txt 1000arch")
        print "done ",arch

f1.close()
	
