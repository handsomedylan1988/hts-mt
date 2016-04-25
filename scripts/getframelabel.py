import os

STATENUM=5
files=os.listdir("align")
statedurs=[]
phonedur=0
label=""
if not os._exists("frame"):
    os.mkdir("frame")
for file in files:
    filepath=os.path.join("align",file)
    outfilepath=os.path.join("frame",file)
    fp_out=open(outfilepath,'w')
    with open (filepath) as fp:
        lines=fp.readlines()
        for idx in xrange(len(lines)):
            data=lines[idx].strip().split()
            if idx%STATENUM==0:
                label=data[2]
                phonestart=int(data[0])/50000
            statedur=(int(data[1])-int(data[0]))/50000
            statedurs.append(statedur)
            if idx%STATENUM==STATENUM-1:
                phonedur=int(data[1])/50000-phonestart
                k=0
                for x in xrange(STATENUM):
                    for j in xrange(statedurs[x]):
                        stateforward=j+1
                        statebackward=statedurs[x]-j
                        phoneforward=k+1
                        phonebackward=phonedur-k
                        #print label,stateforward,statebackward,statedurs[x],phoneforward,phonebackward,phonedur
                        fp_out.write("%s %d %d %d %d %d %d\n" % (label,stateforward,statebackward,statedurs[x],phoneforward,phonebackward,phonedur))
                        k=k+1
                        #raw_input()
                statedurs=[]









