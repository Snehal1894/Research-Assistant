import sys
import os

def main(opname,op):

	olines=[]
	arch=0
	currlist=[]
	seqnums=[]
	#print len(sys.argv)
	#nseqs=int(sys.argv[len(sys.argv)-1])
	nseqs=1000
	fw = open(opname+".txt","w")
	
	for i in op:
	#for i in range(2,len(sys.argv)-1):
		#fname=sys.argv[i]
		#chlines=open(fname,'r').read().splitlines()
		fname=i.strip('\n')
		#print fname
		chlines=open(fname,'r').read().splitlines()
		for j in range(1,len(chlines)):
			seqnum=int(chlines[j].split()[1])
			olines+=[(seqnum,chlines[j].split()[0],chlines[j].split()[8],chlines[j].split()[5])]
			seqnums+=[seqnum]
			arch=max(arch,int(chlines[j].split()[0]))

	for n in range(1,nseqs+1):
		if n not in seqnums:
			olines+=[(n,arch+1,"NNN",0.0)]	

	olines.sort()	

	i=0
	temp=[]
	while i<len(olines):
		temp=[]
		o1=olines[i]
		temp+=[(o1[3],o1[0],o1[1],o1[2])]
		if i+1<len(olines):
			j=i+1
			while j<len(olines) and o1[0]==olines[j][0] :
				temp+=[(olines[j][3],olines[j][0],olines[j][1],olines[j][2])]
				j+=1
			temp.sort(reverse=True)
			fw.write(str(temp[0][2])+"\t"+str(temp[0][1])+"\t"+temp[0][3]+"\t"+str(temp[0][0])+"\n")
			i=j
		else:
			fw.write(str(o1[1])+"\t"+str(o1[0])+"\t"+o1[2]+"\t"+str(o1[3])+"\n")
			i+=1
	fw.close()

if __name__=="__main__":
	main()
