# -*- coding: utf-8 -*-
import pylab as pl
import numpy as np
def slidwindow( result ):
    N=5
    meanN=[0,]
    baseline=sum(result[0])/len(result[0])
    for i,data in enumerate( result[0] ):
        result[0][i]=abs(result[0][i]-baseline)
    pl.figure()
    pl.plot(result[0])
    for i,data in enumerate(result[0]):
        meanN.append(sum(result[0][i:i+5])/N)
    pl.figure()
    pl.plot(meanN)