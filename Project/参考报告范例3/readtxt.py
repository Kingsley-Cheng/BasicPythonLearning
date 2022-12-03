def readtxt(dir):
    ch1=[0,]
    ch2=[0,]
    ch3=[0,]
    ch4=[0,]
    ch5=[0,]
    ch6=[0,]
    fh=open(dir)
    for data in fh:
        ch1.append(int(data[0:4]))
        ch2.append(int(data[4:8]))
        ch3.append(int(data[8:12]))
        ch4.append(int(data[12:16]))
        ch5.append(int(data[16:20]))
        ch6.append(int(data[20:24]))
    return ch1,ch2,ch3,ch4,ch5,ch6
    #print ch1,ch2,ch3,ch4,ch5
    fh.close()