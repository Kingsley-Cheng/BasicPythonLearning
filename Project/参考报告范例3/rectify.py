import pylab as pl
import numpy as np
def rectify( result ):
    baseline=sum(result[0])/len(result[0])
    for i in range(len(result[0])):
        result[0][i]=abs(result[0][i]-baseline)
    pl.plot(result[0])
    return result