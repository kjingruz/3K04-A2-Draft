import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
#import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def addToFile():

     f = open('sampleText.txt', 'r')
     xval,yval = f.readline().split(',')
     f.close()

     xnum = int(xval)
     ynum = int(yval)


     f = open('sampleText.txt', 'a')
    # writeVal = str(xnum)+","+str(ynum)+'\n'
     writeVal = str(random.randrange(0,10))+','+str(random.randrange(0,10))+'\n'
     f.write(writeVal)
     f.close()
     

def animate(i):

    addToFile()#update vals

    pullData = open("sampleText.txt","r").read()                                 # must use txt file for input, else graph wont update
    #pullData.close()

    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)



ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
