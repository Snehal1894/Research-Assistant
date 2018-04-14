import os

f1=os.popen("ls reqfasta")
s1=f1.readlines()

for tf in s1:
    tf=tf.rstrip('\n')
    f2=os.popen("ls reqfasta/"+tf)
    os.popen("mkdir Logos/"+tf)
    s2=f2.readlines()
    for fl in s2:
        if "fa_archs.txt" in fl:
            fl=fl.rstrip('\n')
            cmd2="python archs2svg.py reqfasta/"+tf+"/"+fl+" > Logos/"+tf+"/"+fl.split('fa')[0]+"svg"
            print cmd2
            os.popen(cmd2)
