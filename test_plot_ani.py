import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

inc = 1

def addToFile():
     f = open('sampleText.txt', 'a')
     f.write('\n13,2\n14,7')
     f.close()
     inc+=1
     print(inc)

def animate(i):

    #addToFile()#update vals

    pullData = open("sampleText.txt","r")
    pullData.read()                                 # must use txt file for input, else graph wont update
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
