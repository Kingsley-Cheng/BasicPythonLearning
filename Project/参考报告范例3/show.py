import pylab as pl
def show(result):
    pl.plot(range(len(result[0])-1),result[0][1:len(result[0])],'r')
    pl.legend('1')
    pl.plot(range(len(result[1])-1),result[1][1:len(result[1])])
    pl.plot(range(len(result[2])-1),result[2][1:len(result[2])])
    pl.plot(range(len(result[3])-1),result[3][1:len(result[3])])
    pl.plot(range(len(result[4])-1),result[4][1:len(result[4])])
    pl.plot(range(len(result[5])-1),result[5][1:len(result[5])])
    pl.xlabel(u'Time')
    pl.ylabel(u'Volt')
    pl.title(u'Time Scale EMG')
    pl.xlim(0,len(result[0])+50)
    pl.ylim(0,max(result[0])+500)
    