# -*- coding: utf-8 -*-
import pylab as pl
import numpy as np
def fft( result ):
    fs=1000
    N=len(result[0])
    f=[0,]
    
    nr=np.fft.fft(result[0])
    r=abs(nr[1:N/2])
    
    for n in range(N):
        f.append(fs/N*n)
    f.pop(0)
    
    pl.figure()
    pl.plot(f[0:len(r)],r)
#    pl.xlim(0,len(r)+100)
#    pl.ylim(0,max(r)+1000)
    pl.xlabel(u'Frequency')
    pl.ylabel(u'Amplitude')
    pl.title(u'Power Spectrum of EMG')
    return r