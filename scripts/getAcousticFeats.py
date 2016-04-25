#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Dylan @ 2016-04-24 20:23:07

import os 
import numpy
import sPickle

labels=[]
NBYTE=(35+1)*3+1 #mgc/lf0(3 windows)/uvflag
for file in [os.path.join("cmp1",f) for f in sorted(os.listdir("cmp1/"))]:
    labelarray = numpy.fromfile(file,dtype=numpy.float32)
    assert len(labelarray)%NBYTE==0 
    nFrame= len(labelarray)/NBYTE
    labels+=list(labelarray.reshape(nFrame,NBYTE))
    #print nFrame

labels=numpy.array(labels)
l_mean=labels.mean(axis=0)
l_std=labels.std(axis=0)

print len(labels)
labels=(labels-l_mean)/l_std

with open("labels.pkl","wb") as fp:
    sPickle.s_dump(l_mean,fp)
    sPickle.s_dump(l_std,fp)
    sPickle.s_dump(labels,fp)



