import serial
import serial.tools.list_ports
import struct
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# import time


class pacemakerSerial:

    def __init__(self):
        # Mac port, for windows you have to find the ports yourself lmao
        self.frdm_port = "/dev/cu.usbmodem0000001234561"

        # Windows port, check COM port in device manager
        # win_port = "COM4"

        # B = uint8
        # f = single
        # H = uint16
        # d = double ( 8 bytes)

        # parameter values to send to pacemaker
        self.Start = b'\x16'
        self.SYNC = b'\x22'
        self.Fn_set = b'\x55'
        self.Pacing_mode = struct.pack("B", 1)
        self.LRL = struct.pack("B", 1)
        self.URL = struct.pack("B", 1)
        self.MSR = struct.pack("B", 1)
        self.A_V_PA = struct.pack("f", 1.0)
        self.A_V_PW = struct.pack("B", 1)
        self.A_V_Sense = struct.pack("B", 1)
        self.A_V_R = struct.pack("H", 1)
        self.PVARP = struct.pack("H", 1)
        self.Act_thres = struct.pack("B", 1)
        self.React_time = struct.pack("B", 1)
        self.Response_factor = struct.pack("B", 1)
        self.Recovery_time = struct.pack("B", 1)

        # values to read for ECG
        self.Atr = 0.0
        self.Vnt = 0.0

    # send current parameter values to pacemaker
    def send_param(self):
        # create signal to send
        Signal_set = self.Start + self.Fn_set + self.Pacing_mode + self.LRL + self.URL + self.MSR + self.A_V_PA + self.A_V_PW + self.A_V_Sense + self.A_V_R + self.PVARP + self.Act_thres + self.React_time + self.Response_factor + self.Recovery_time

        with serial.Serial(self.frdm_port, 115200) as pacemaker:
            pacemaker.write(Signal_set)

    # recieve Atr and Vnt values from pacemaker for ECG
    def get_echo(self):
        # create signal to send
        Signal_echo = self.Start + self.SYNC + self.Pacing_mode + self.LRL + self.URL + self.MSR + self.A_V_PA + self.A_V_PW + self.A_V_Sense + self.A_V_R + self.PVARP + self.Act_thres + self.React_time + self.Response_factor + self.Recovery_time

        with serial.Serial(self.frdm_port, 115200) as pacemaker:
            pacemaker.write(Signal_echo)
            data = pacemaker.read(34)
            self.Atr = struct.unpack("d", data[18:26])[0]
            self.Vnt = struct.unpack("d", data[26:34])[0]

            print(self.Atr)
            print(self.Vnt)

    def update(self, database):

        self.Pacing_mode = struct.pack("B", 1)
        self.LRL = struct.pack("B", 1)
        self.URL = struct.pack("B", 1)
        self.MSR = struct.pack("B", 1)
        self.A_V_PA = struct.pack("f", 1.0)
        self.A_V_PW = struct.pack("B", 1)
        self.A_V_Sense = struct.pack("B", 1)
        self.A_V_R = struct.pack("H", 1)
        self.PVARP = struct.pack("H", 1)
        self.Act_thres = struct.pack("B", 1)
        self.React_time = struct.pack("B", 1)
        self.Response_factor = struct.pack("B", 1)
        self.Recovery_time = struct.pack("B", 1)

    def getAtr(self):
        return self.Atr

    def getVnt(self):
        return self.Vnt


class animateGraph:

    # pass in pacemakerSerial object on  init, assumes you already have on instantiated
    def __init__(self, pacemakerSerial):
        # for serial com
        self.pacemaker = pacemakerSerial

        # for plot
        self.inc = 0
        self.time = 0
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)

    def addToFile(self):

        # saved as: time, Atr, Vnt
        f = open('sampleText.txt', 'r')
        self.time = f.readline().split(',')[0]  # pulls most recent time to increment
        self.inc += float(0.5)
        self.time += str(self.inc)
        f.close()

        # pulls new Atr and Vnt values from pacemaker... loop this to get more values , but keep animate interval in mind
        self.pacemaker.get_echo()

        f = open('EGRAM_vals.txt', 'a')
        writeVal = str(self.time) + ',' + str(self.pacemaker.getAtr()) + ',' + str(self.pacemaker.getVnt()) + '\n'
        f.write(writeVal)
        f.close()

    def animate(self, i):

        self.addToFile()  # update vals

        pullData = open("EGRAM_vals.txt", "r").read()  # must use txt file for input, else graph wont update

        # saved as: time, Atr, Vnt
        dataArray = pullData.split('\n')
        tar = []
        aar = []
        var = []
        for eachLine in dataArray:
            if len(eachLine) > 1:
                t, a, v = eachLine.split(',')
                tar.append(str(t))
                aar.append(str(a))
                var.append(str(v))
        self.ax1.clear()
        self.ax1.plot(tar, aar, label="Atrial")
        self.ax1.plot(tar, var, label="Ventrical")
        self.ax1.legend()

    # run this to open the plot
    def showPlot(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=10)  # refresh every 10ms
        plt.show()


b1 = pacemakerSerial()
a1 = animateGraph(b1)
a1.showPlot()
