import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import serial

ser = serial.Serial('COM4',115200) #windows

print(ser.name)
# hex(value) outputs a string :(
enter = [0x16, 0x55, 0x1, 0x32, 0x32, 0x32, 0x5, 0x1, 0x0, 0x96, 0x96, 0x1, 0xA, 0x1, 0x2] #hex
ser.write(enter)
print("test file sent")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def updateFile():

    #ask for new values
     enter = [0x16, 0x61, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0] #hex
     ser.write(enter)

    #read values
     xin = text = ser.read()
     print(text)
     yin = text = ser.read()
     print(text)

     f = open('sampleText.txt', 'r')
     xval,yval = f.readline().split(',')
     f.close()

     xnum = int(xval)
     ynum = int(yval)


     f = open('sampleText.txt', 'a')
    # writeVal = str(xnum)+","+str(ynum)+'\n'
    # writeVal = str(random.randrange(0,10))+','+str(random.randrange(0,10))+'\n'
     writeVal = str(xin)+','+str(yin)+'\n'
     f.write(writeVal)
     f.close()

def animate(i):

    updateFile()#update vals
    #print("test")

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

print("before")

ani = animation.FuncAnimation(fig, animate, interval=1)
print("ani")
plt.show()
print("show")
plt.close()
print("close")

serial.close()#do this earlier??